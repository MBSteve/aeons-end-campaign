#!/usr/bin/env python3
"""
Image Generator for Aeon's End Campaign
========================================
Reads image prompt files from the ImagePrompts/ directory and generates images
using the OpenRouter API with the Nano Banana Pro (Gemini 3 Pro Image) model.

Images are saved to the paths specified in each prompt file.

Requirements:
    pip install requests

Usage:
    python scripts/generate_images.py                          # Generate all pending prompts
    python scripts/generate_images.py ImagePrompts/SomeFile.md # Generate a specific prompt
    python scripts/generate_images.py --list                   # List pending prompts
    python scripts/generate_images.py --dry-run                # Show what would be generated
"""

import os
import sys
import json
import re
import base64
import argparse
from pathlib import Path
from datetime import datetime

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
IMAGE_MODEL = "google/gemini-3-pro-image"

# Automatically appended to every generated image prompt per StyleGuide.md
STYLE_GUIDE_CONSTRAINTS = (
    "Cinematic dark-fantasy realism, photorealistic high-end fantasy game cinematic, "
    "grounded medieval Gothic setting, mature naturalistic character design, "
    "realistic ageing and skin texture, weathered layered fabrics and tarnished metal, "
    "restrained practical costume, dramatic chiaroscuro lighting, "
    "warm candlelight against cool ambient shadows, muted charcoal and earthy colour palette, "
    "subtle atmospheric haze, shallow depth of field, highly detailed face, "
    "tactile materials, sombre dignified mood, natural proportions, "
    "realistic film colour grading, 85mm portrait photography, subtle film grain, "
    "sharp facial focus, softly blurred Gothic background. "
    "AVOID: steampunk, brass machinery, gears, goggles, pipes, Victorian industrial, "
    "excessive ornamentation, glowing runes, neon lighting, colourful magic effects, "
    "anime, comic book style, obvious digital painting, visible brush strokes, "
    "glossy plastic skin, beauty retouching, fashion photography, perfect symmetry, "
    "young-looking face, exaggerated armour, oversized pauldrons, ornate crown, "
    "sexualised costume, heroic pose, smiling, saturated colours, clean new clothing, "
    "bright daylight, flat lighting, generic fantasy illustration, cartoon, concept sketch, "
    "low-detail background."
)

# Read API key from VS Code's secret storage mechanism.
# The key is stored in chatLanguageModels.json as ${input:chat.lm.secret.b4cc8e9}.
# We look for it in environment variables or a local .env file.
API_KEY = os.environ.get("OPENROUTER_API_KEY")

if not API_KEY:
    # Try reading from a .env file in the repo root
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("OPENROUTER_API_KEY="):
                    API_KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break

# ---------------------------------------------------------------------------
# Prompt file parsing
# ---------------------------------------------------------------------------

def is_prompt_completed(filepath: str) -> bool:
    """Check if a prompt file's Status section indicates the image is already generated."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for the Status section and check if Image generated is checked
    # Pattern: [x] Image generated
    status_section = re.search(r"## Status\s*\n(.*?)(?:\n##|\Z)", content, re.DOTALL)
    if not status_section:
        return False

    status_text = status_section.group(1)
    return bool(re.search(r"\[x\]\s*Image generated", status_text, re.IGNORECASE))


def parse_prompt_file(filepath: str) -> dict | None:
    """Parse a prompt Markdown file and extract structured fields."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fields = {}
    current_key = None
    current_value: list[str] = []

    # Known field names from the image prompt template
    known_fields = [
        "asset name", "purpose", "canonical facts", "required visual elements",
        "prohibited elements", "composition", "mood", "lighting",
        "colour palette", "art style", "aspect ratio", "intended repository path",
        "markdown reference"
    ]

    # Skip StyleGuide.md
    if Path(filepath).name == "StyleGuide.md":
        return None

    for line in content.split("\n"):
        # Check if line contains a known field header (with or without bold, bullet, or trailing colon)
        stripped = line.strip()

        # Stop appending when we hit a Markdown heading (##) or horizontal rule (---)
        if re.match(r"^##", stripped) or stripped == "---":
            if current_key and current_value:
                fields[current_key] = "\n".join(current_value).strip()
            current_key = None
            current_value = []
            continue

        # Match: "- **Asset Name**: ...", "**Asset Name**: ...", "Asset Name: ...", etc.
        match = re.match(r"^(?:-\s+)?(?:\*\*)?([^*\n:]+?)(?:\*\*)?\s*:\s*(.*)", stripped)
        if match:
            field_name = match.group(1).strip().lower()
            field_rest = match.group(2).strip()
            # Save previous field
            if current_key and current_value:
                fields[current_key] = "\n".join(current_value).strip()
            if field_name in known_fields:
                current_key = field_name
                current_value = [field_rest] if field_rest else []
            else:
                current_key = None
                current_value = []
        elif current_key and stripped:
            current_value.append(stripped)
        elif current_key and not stripped:
            current_value.append("")

    if current_key and current_value:
        fields[current_key] = "\n".join(current_value).strip()

    # Validate required fields
    if "asset name" not in fields:
        print(f"  WARNING: No 'Asset Name' found in {filepath}, skipping.")
        return None

    return fields


def build_image_prompt(fields: dict) -> str:
    """Build a natural-language image generation prompt from parsed fields."""
    parts = []

    parts.append(f"Generate an illustration for: {fields.get('asset name', 'Unknown asset')}.")

    if "purpose" in fields:
        parts.append(f"Purpose: {fields['purpose']}")

    if "canonical facts" in fields:
        parts.append(f"Key canonical facts: {fields['canonical facts']}")

    if "required visual elements" in fields:
        parts.append(f"Must include: {fields['required visual elements']}")

    if "prohibited elements" in fields:
        parts.append(f"Do NOT include: {fields['prohibited elements']}")

    if "composition" in fields:
        parts.append(f"Composition: {fields['composition']}")

    if "mood" in fields:
        parts.append(f"Mood and atmosphere: {fields['mood']}")

    if "lighting" in fields:
        parts.append(f"Lighting: {fields['lighting']}")

    if "colour palette" in fields:
        parts.append(f"Colour palette: {fields['colour palette']}")

    if "art style" in fields:
        parts.append(f"Art style: {fields['art style']}")

    if "aspect ratio" in fields:
        parts.append(f"Aspect ratio: {fields['aspect ratio']}")

    # Append the campaign style guide to every prompt
    parts.append(STYLE_GUIDE_CONSTRAINTS)

    return "\n\n".join(parts)


def get_output_path(fields: dict, repo_root: Path) -> Path:
    """Determine the output image path from the prompt fields."""
    path_str = fields.get("intended repository path", "")
    if path_str:
        # Strip backticks and surrounding whitespace (e.g., "`Maps/foo.png`" → "Maps/foo.png")
        path_str = path_str.strip().strip("`").strip()
        return repo_root / path_str
    # Fallback: derive from asset name
    asset_name = fields.get("asset name", "unknown").replace(" ", "_")
    return repo_root / "Images" / f"{asset_name}.png"


# ---------------------------------------------------------------------------
# Image generation
# ---------------------------------------------------------------------------

def generate_image(prompt: str, api_key: str, reference_images: list[Path] | None = None) -> bytes | None:
    """Call OpenRouter to generate an image using the Gemini image model."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Build multimodal content: text + optional reference images
    content_parts = [{"type": "text", "text": prompt}]

    if reference_images:
        print(f"  Including {len(reference_images)} reference image(s)...")
        for img_path in reference_images:
            if img_path.exists():
                with open(img_path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode("utf-8")
                ext = img_path.suffix.lstrip(".")
                content_parts.append({
                    "type": "image_url",
                    "image_url": f"data:image/{ext};base64,{b64}"
                })
                print(f"    Added: {img_path.name}")
            else:
                print(f"    WARNING: Reference image not found: {img_path}")

    payload = {
        "model": IMAGE_MODEL,
        "messages": [
            {
                "role": "user",
                "content": content_parts,
            }
        ],
        "max_tokens": 8192,
    }

    print(f"  Calling OpenRouter with model '{IMAGE_MODEL}'...")
    response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=120)

    if response.status_code != 200:
        print(f"  ERROR: OpenRouter returned status {response.status_code}")
        print(f"  {response.text[:500]}")
        return None

    result = response.json()

    # Debug: dump the full response structure (keys only, not full data)
    print(f"  Response keys: {list(result.keys())}")
    if "choices" in result and result["choices"]:
        choice = result["choices"][0]
        print(f"  Choice keys: {list(choice.keys())}")
        message = choice.get("message", {})
        if message:
            print(f"  Message keys: {list(message.keys())}")
            # Check for images array (OpenRouter-specific for Gemini image models)
            if "images" in message:
                print(f"  Found {len(message['images'])} image(s) in message.images")
            content = message.get("content")
            print(f"  Content type: {type(content).__name__}, preview: {str(content)[:200] if content else 'None'}")
        else:
            print(f"  No message in choice")
            content = None
    else:
        print("  ERROR: No choices in response.")
        print(f"  Response: {json.dumps(result, indent=2)[:1000]}")
        return None

    # Parse the response for image data.
    # Gemini image models on OpenRouter may return images in:
    # 1. message.images[] — OpenRouter-specific array of image URLs/data
    # 2. message.content as a list of parts with inlineData or image_url

    # Check for message.images first (OpenRouter format)
    if "images" in message and message["images"]:
        for img in message["images"]:
            print(f"  Image entry type: {type(img).__name__}")
            if isinstance(img, dict):
                print(f"  Image keys: {list(img.keys())}")
                # Try to find image data from various possible keys
                # OpenRouter may return: {"url": "...", "detail": "..."} or {"image_url": {"url": "..."}}
                img_url = img.get("url", "") or img.get("image_url", "")
                if isinstance(img_url, dict):
                    img_url = img_url.get("url", "")
                if isinstance(img_url, str):
                    if img_url.startswith("data:image"):
                        b64 = img_url.split(",", 1)[1]
                        return base64.b64decode(b64)
                    if img_url.startswith("http"):
                        img_resp = requests.get(img_url, timeout=60)
                        if img_resp.status_code == 200:
                            return img_resp.content
                # Check for base64 data directly
                b64_data = img.get("data", "") or img.get("b64_json", "")
                if b64_data and isinstance(b64_data, str):
                    return base64.b64decode(b64_data)
            elif isinstance(img, str):
                if img.startswith("data:image"):
                    b64 = img.split(",", 1)[1]
                    return base64.b64decode(b64)
                if img.startswith("http"):
                    img_resp = requests.get(img, timeout=60)
                    if img_resp.status_code == 200:
                        return img_resp.content

    # Check content as a list of parts
    if isinstance(content, list):
        for part in content:
            if isinstance(part, dict):
                # Check for inline image data
                if "inlineData" in part:
                    b64 = part["inlineData"].get("data", "")
                    if b64:
                        return base64.b64decode(b64)
                if "image_url" in part:
                    img_url = part["image_url"].get("url", "")
                    if img_url.startswith("data:image"):
                        b64 = img_url.split(",", 1)[1]
                        return base64.b64decode(b64)
                    # Could be a remote URL — download it
                    if img_url.startswith("http"):
                        img_resp = requests.get(img_url, timeout=60)
                        if img_resp.status_code == 200:
                            return img_resp.content
    elif isinstance(content, str):
        # Try to find a base64 data URL in the string
        match = re.search(r"data:image/[^;]+;base64,([A-Za-z0-9+/=]+)", content)
        if match:
            return base64.b64decode(match.group(1))
        # Try to find a markdown image reference
        match = re.search(r"!\[.*?\]\((https?://[^)]+)\)", content)
        if match:
            img_resp = requests.get(match.group(1), timeout=60)
            if img_resp.status_code == 200:
                return img_resp.content

    print(f"  WARNING: Could not extract image data from response.")
    print(f"  Content preview: {str(content)[:300]}")
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def find_prompt_files(repo_root: Path) -> list[Path]:
    """Find all prompt files in the ImagePrompts directory."""
    prompts_dir = repo_root / "ImagePrompts"
    if not prompts_dir.exists():
        print(f"ImagePrompts directory not found at {prompts_dir}")
        return []

    prompt_files = sorted(prompts_dir.glob("*.md"))
    # Exclude the template file
    prompt_files = [p for p in prompt_files if p.name != "ImagePromptTemplate.md"]
    return prompt_files


def main():
    parser = argparse.ArgumentParser(
        description="Generate images for Aeon's End campaign from prompt files."
    )
    parser.add_argument(
        "prompts", nargs="*",
        help="Specific prompt file(s) to generate. If omitted, generates all pending."
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List all pending prompt files and exit."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be generated without actually generating."
    )
    parser.add_argument(
        "--repo-root", default=None,
        help="Path to the repo root. Defaults to the parent of the scripts/ directory."
    )
    args = parser.parse_args()

    # Determine repo root
    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent
        # If the repo root contains an AeonsEndCampaign subdirectory, use that
        campaign_dir = repo_root / "AeonsEndCampaign"
        if campaign_dir.is_dir():
            repo_root = campaign_dir

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set.")
        print("Set it as an environment variable or create a .env file in the repo root:")
        print("  OPENROUTER_API_KEY=your-key-here")
        print("\nYou can get your key from the VS Code chatLanguageModels.json file.")
        print("Look for the secret referenced as ${input:chat.lm.secret.b4cc8e9}.")
        sys.exit(1)

    # Find prompt files
    if args.prompts:
        prompt_paths = [Path(p) for p in args.prompts]
    else:
        prompt_paths = find_prompt_files(repo_root)

    if args.list:
        if prompt_paths:
            print(f"Pending prompt files ({len(prompt_paths)}):")
            for p in prompt_paths:
                print(f"  {p.relative_to(repo_root)}")
        else:
            print("No pending prompt files found.")
        return

    if not prompt_paths:
        print("No prompt files to generate.")
        return

    print(f"Found {len(prompt_paths)} prompt file(s) to process.\n")

    for prompt_path in prompt_paths:
        rel_path = prompt_path.relative_to(repo_root) if prompt_path.is_relative_to(repo_root) else prompt_path

        # Skip already-completed prompts
        if is_prompt_completed(str(prompt_path)):
            print(f"Skipping (already generated): {rel_path}")
            continue

        print(f"Processing: {rel_path}")

        fields = parse_prompt_file(str(prompt_path))
        if fields is None:
            continue

        asset_name = fields.get("asset name", "unknown")
        print(f"  Asset: {asset_name}")

        prompt = build_image_prompt(fields)
        output_path = get_output_path(fields, repo_root)

        print(f"  Output: {output_path.relative_to(repo_root)}")

        if args.dry_run:
            print(f"  [DRY RUN] Would generate image. Prompt preview:")
            print(f"  ---")
            for line in prompt.split("\n")[:5]:
                print(f"  {line}")
            print(f"  ---")
            continue

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Generate the image
        image_data = generate_image(prompt, API_KEY)
        if image_data is None:
            print(f"  FAILED to generate image for '{asset_name}'")
            continue

        # Save the image
        with open(output_path, "wb") as f:
            f.write(image_data)

        file_size_kb = len(image_data) / 1024
        print(f"  SAVED ({file_size_kb:.1f} KB)")

        # Save a timestamped backup copy
        backup_dir = repo_root / "Backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        stem = output_path.stem
        suffix = output_path.suffix
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"{stem}_{timestamp}{suffix}"
        with open(backup_path, "wb") as f:
            f.write(image_data)
        print(f"  BACKED UP to Backups/{backup_path.name}")

        # Update the markdown reference in the prompt file
        md_ref = fields.get("markdown reference", "")
        if md_ref:
            print(f"  Markdown reference: {md_ref}")

        print()

    print("Done.")


if __name__ == "__main__":
    main()