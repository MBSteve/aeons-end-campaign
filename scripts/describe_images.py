#!/usr/bin/env python3
"""
Describe Reference Images
=========================
Sends each reference image (front.jpg, back.jpg) to a multimodal LLM via OpenRouter
to get a detailed textual description of the character's appearance, equipment, pose,
expression, colours, and background. Saves the descriptions alongside the images.

Usage:
    python scripts/describe_images.py                          # Describe all mages and nemeses
    python scripts/describe_images.py --mage "Adelheim"        # Describe a specific mage
    python scripts/describe_images.py --nemesis "Carapace"     # Describe a specific nemesis
    python scripts/describe_images.py --list                   # List what would be described
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
# Use a fast capable model for description — doesn't need image generation
DESCRIBE_MODEL = "google/gemini-3-pro-image"

API_KEY = os.environ.get("OPENROUTER_API_KEY")
if not API_KEY:
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("OPENROUTER_API_KEY="):
                    API_KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break

DESCRIBE_SYSTEM_PROMPT = (
    "You are a meticulous visual analyst. Describe the provided image in extreme detail. "
    "Focus on what is physically visible: the character's face (age, expression, features), "
    "hair, build, pose, clothing (textures, colours, layers, condition), equipment (weapons, "
    "armour, accessories, crystals, tools), the background setting, the colour palette, "
    "the lighting direction and quality, and any magical or special effects. "
    "Be objective and concrete — describe what is actually in the image, not what you infer "
    "about the character's personality. Include body proportions and how much of the body is visible. "
    "If hands or feet are visible, describe what they are doing."
)

DESCRIBE_USER_PROMPT = (
    "Describe this image in extreme detail as if you are writing reference notes for a "
    "photorealistic CGI artist who needs to recreate this character from scratch. "
    "Cover: face and expression, hair, age, build, pose, full outfit (every visible layer, "
    "colours, materials, wear-and-tear), visible equipment or props, hands and what they are "
    "doing, background environment, lighting, colour palette, any magical effects or glows. "
    "Be exhaustive — every visible detail matters."
)


def describe_image(image_path: Path) -> str | None:
    """Send a single image to the LLM and get back a detailed text description."""
    if not API_KEY:
        print("  ERROR: OPENROUTER_API_KEY not set.")
        return None

    if not image_path.exists():
        print(f"  ERROR: Image not found: {image_path}")
        return None

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    # Read and base64-encode the image
    with open(image_path, "rb") as f:
        b64 = __import__("base64").b64encode(f.read()).decode("utf-8")
    ext = image_path.suffix.lstrip(".")

    payload = {
        "model": DESCRIBE_MODEL,
        "messages": [
            {
                "role": "system",
                "content": [{"type": "text", "text": DESCRIBE_SYSTEM_PROMPT}],
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": DESCRIBE_USER_PROMPT},
                    {"type": "image_url", "image_url": f"data:image/{ext};base64,{b64}"},
                ],
            },
        ],
        "max_tokens": 4096,
    }

    print(f"    Describing {image_path.name}...")
    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=300)
        if response.status_code != 200:
            print(f"    ERROR: API returned {response.status_code}: {response.text[:300]}")
            return None

        result = response.json()
        choices = result.get("choices", [])
        if not choices:
            print(f"    ERROR: No choices in response: {json.dumps(result)[:300]}")
            return None

        text = choices[0].get("message", {}).get("content", "")
        if not text:
            print(f"    WARNING: Empty content in response")
            return None

        return text.strip()

    except Exception as e:
        print(f"    ERROR: {e}")
        return None


def describe_asset(asset_dir: Path, asset_name: str, asset_type: str):
    """Describe all images for a single asset (mage or nemesis)."""
    print(f"\n{'='*60}")
    print(f"{asset_type}: {asset_name}")
    print(f"{'='*60}")

    if not asset_dir.exists():
        print(f"  Directory not found: {asset_dir}")
        return

    # Skip if already described
    combined_path = asset_dir / "descriptions.json"
    if combined_path.exists():
        print(f"  Already described (descriptions.json exists), skipping.")
        return

    image_files = sorted(asset_dir.glob("*.jpg")) + sorted(asset_dir.glob("*.png"))

    if not image_files:
        print(f"  No images found.")
        return

    descriptions = {}
    for img_path in image_files:
        desc = describe_image(img_path)
        if desc:
            descriptions[img_path.name] = desc
            # Also save individual text file alongside the image
            desc_path = img_path.with_suffix(".txt")
            desc_path.write_text(desc, encoding="utf-8")
            print(f"    Saved description to {desc_path.name}")

    # Save combined description file
    if descriptions:
        combined_path = asset_dir / "descriptions.json"
        combined = {
            "asset": asset_name,
            "type": asset_type,
            "generated": datetime.now().isoformat(),
            "descriptions": descriptions,
        }
        with open(combined_path, "w", encoding="utf-8") as f:
            json.dump(combined, f, indent=2, ensure_ascii=False)
        print(f"  Saved combined descriptions to descriptions.json")


def main():
    parser = argparse.ArgumentParser(
        description="Generate detailed textual descriptions of reference images."
    )
    parser.add_argument("--mage", default=None, help="Specific mage to describe")
    parser.add_argument("--nemesis", default=None, help="Specific nemesis to describe")
    parser.add_argument("--mages", action="store_true", help="Describe all mages")
    parser.add_argument("--nemeses", action="store_true", help="Describe all nemeses")
    parser.add_argument("--list", action="store_true", help="List what would be described")
    parser.add_argument(
        "--repo-root", default=None,
        help="Path to the repo root. Defaults to script's parent."
    )
    args = parser.parse_args()

    # Determine repo root
    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent
    ref_root = repo_root / "AeonsEndCampaign" / "ReferenceImages"

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set.")
        print("Set it as an environment variable or add to a .env file.")
        sys.exit(1)

    # Gather the targets
    targets = []  # list of (directory, name, type_label)

    if args.mage:
        # Single mage
        mage_dir = ref_root / "Mages" / args.mage
        targets.append((mage_dir, args.mage, "Mage"))
    elif args.nemesis:
        nemesis_dir = ref_root / "Nemeses" / args.nemesis
        targets.append((nemesis_dir, args.nemesis, "Nemesis"))
    else:
        if args.mages or not args.nemeses:
            mages_dir = ref_root / "Mages"
            if mages_dir.exists():
                for d in sorted(mages_dir.iterdir()):
                    if d.is_dir():
                        targets.append((d, d.name, "Mage"))
        if args.nemeses or not args.mages:
            nemeses_dir = ref_root / "Nemeses"
            if nemeses_dir.exists():
                for d in sorted(nemeses_dir.iterdir()):
                    if d.is_dir():
                        targets.append((d, d.name, "Nemesis"))

    if not targets:
        print("No targets found. Check that ReferenceImages/Mages and ReferenceImages/Nemeses exist.")
        return

    if args.list:
        print(f"Would describe images for {len(targets)} asset(s):")
        for _, name, typ in targets:
            print(f"  [{typ}] {name}")
        return

    print(f"Found {len(targets)} asset(s) to describe.\n")

    for asset_dir, name, typ in targets:
        describe_asset(asset_dir, name, typ)

    print(f"\nDone. Descriptions saved as .txt files alongside images and as descriptions.json.")


if __name__ == "__main__":
    main()