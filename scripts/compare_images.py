#!/usr/bin/env python3
"""
Style Comparison Tool for Aeon's End Campaign
==============================================
Compares two images using the Nano Banana Pro (Gemini) model via OpenRouter
and produces a detailed style comparison report.

Requirements:
    pip install requests

Usage:
    python scripts/compare_images.py <image_a> <image_b>
    python scripts/compare_images.py Images/NPCs/Councilor_Sera.png Images/NPCs/Kellan_Voss.png
"""

import os
import sys
import json
import base64
import argparse
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
COMPARE_MODEL = "google/gemini-3-pro-image"  # Nano Banana Pro — multimodal

# Read API key
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

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def image_to_base64(filepath: str) -> str:
    """Read an image file and return a base64 data URL."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")

    ext = path.suffix.lower()
    mime_map = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    mime = mime_map.get(ext, "image/png")
    return f"data:{mime};base64,{data}"


def compare_images(image_a_path: str, image_b_path: str, api_key: str) -> str:
    """Send two images to the model for style comparison."""
    print(f"Loading image A: {image_a_path}")
    img_a_b64 = image_to_base64(image_a_path)

    print(f"Loading image B: {image_b_path}")
    img_b_b64 = image_to_base64(image_b_path)

    comparison_prompt = (
        "You are an art director reviewing two images for a dark fantasy campaign. "
        "The campaign's required style is:\n\n"
        "- Hand-painted dark fantasy\n"
        "- Ink linework with subtle watercolour\n"
        "- Oblique bird's-eye or cinematic perspective\n"
        "- Palette: muted earth tones, slate grey, weathered stone, forest green, ochre\n"
        "- No saturated colours\n"
        "- Lighting: natural, overcast skies, soft sunlight, warm torchlight indoors\n"
        "- Avoid: anime, steampunk, photorealism, concept art, comic book, 3D render, digital painting, video game UI\n"
        "- Overall feeling: a forgotten medieval world documented by a master cartographer\n\n"
        "Image A is the REFERENCE — it represents the correct campaign style.\n"
        "Image B is the image to EVALUATE against the reference.\n\n"
        "Please provide a detailed comparison covering:\n\n"
        "1. **Overall Style Match**: Does Image B use hand-painted dark fantasy, or does it lean toward photorealism / 3D / digital painting / anime / concept art?\n"
        "2. **Medium & Texture**: Does Image B show ink linework and watercolour texture, or does it look like a digital render?\n"
        "3. **Colour Palette**: Does Image B use muted earth tones, or are there saturated/neon colours?\n"
        "4. **Lighting**: Is the lighting natural and overcast, or is it harsh/artificial?\n"
        "5. **Key Differences**: What are the most important stylistic differences between Image A and Image B?\n"
        "6. **Verdict**: Does Image B match the campaign style? If not, what specific changes would make it match?\n\n"
        "Be direct and specific. This feedback will be used to fix the prompt for Image B."
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": COMPARE_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": comparison_prompt},
                    {"type": "image_url", "image_url": {"url": img_a_b64}},
                    {"type": "image_url", "image_url": {"url": img_b_b64}},
                ],
            }
        ],
        "max_tokens": 4096,
    }

    print(f"\nSending comparison request to {COMPARE_MODEL}...")
    response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=180)

    if response.status_code != 200:
        print(f"ERROR: OpenRouter returned status {response.status_code}")
        print(f"Response: {response.text[:1000]}")
        sys.exit(1)

    result = response.json()

    if "choices" not in result or not result["choices"]:
        print("ERROR: No choices in response.")
        print(json.dumps(result, indent=2)[:1000])
        sys.exit(1)

    content = result["choices"][0]["message"].get("content", "")
    if not content:
        print("ERROR: Empty response content.")
        print(json.dumps(result, indent=2)[:1000])
        sys.exit(1)

    return content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Compare two images for campaign style consistency using Nano Banana Pro."
    )
    parser.add_argument("image_a", help="Path to the REFERENCE image (correct style)")
    parser.add_argument("image_b", help="Path to the image to EVALUATE")
    parser.add_argument(
        "--repo-root", default=None,
        help="Path to the repo root. Defaults to the parent of the scripts/ directory."
    )
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set.")
        print("Set it as an environment variable or create a .env file in the repo root.")
        sys.exit(1)

    # Resolve repo root for relative paths
    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent
        campaign_dir = repo_root / "AeonsEndCampaign"
        if campaign_dir.is_dir():
            repo_root = campaign_dir

    # Resolve image paths
    img_a = Path(args.image_a)
    if not img_a.is_absolute():
        img_a = repo_root / img_a

    img_b = Path(args.image_b)
    if not img_b.is_absolute():
        img_b = repo_root / img_b

    print("=" * 60)
    print("Aeon's End Campaign — Style Comparison")
    print("=" * 60)
    print(f"Reference (correct):  {img_a}")
    print(f"Evaluate (check):     {img_b}")
    print("=" * 60)

    result = compare_images(str(img_a), str(img_b), API_KEY)

    print("\n" + "=" * 60)
    print("COMPARISON RESULT")
    print("=" * 60)
    print(result)
    print("=" * 60)


if __name__ == "__main__":
    main()