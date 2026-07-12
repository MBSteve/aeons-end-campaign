#!/usr/bin/env python3
"""
Generate Image Prompt Files
===========================
Reads the descriptions.json + data.json from each asset's reference image folder
and creates a prompt Markdown file in the ImagePrompts directory.

Usage:
    python scripts/generate_prompts.py                          # All assets
    python scripts/generate_prompts.py --mage "Adelheim"        # Single mage
    python scripts/generate_prompts.py --nemesis "Carapace"     # Single nemesis
    python scripts/generate_prompts.py --list                   # List what would be generated
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

STYLE_GUIDE = (
    "Cinematic dark-fantasy realism, photorealistic high-end fantasy game cinematic, "
    "grounded medieval Gothic setting, mature naturalistic character design, "
    "realistic ageing and skin texture, weathered layered fabrics and tarnished metal, "
    "restrained practical costume, dramatic chiaroscuro lighting, "
    "warm candlelight against cool ambient shadows, muted charcoal and earthy colour palette, "
    "subtle atmospheric haze, shallow depth of field, highly detailed face, "
    "tactile materials, sombre dignified mood, natural proportions, "
    "realistic film colour grading, 35mm environmental portrait, subtle film grain, "
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


def load_json(path: Path) -> dict | None:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def generate_mage_prompt(asset_name: str, descriptions: dict, data: dict | None) -> str:
    """Generate a prompt Markdown file for a mage."""
    lore = data.get("lore", "") if data else ""
    ability = data.get("ability", "") if data else ""
    overview = data.get("overview", "") if data else ""
    strategy = data.get("strategy", "") if data else ""

    desc_front = descriptions.get("front.jpg", "") or descriptions.get("front.png", "")
    desc_back = descriptions.get("back.jpg", "") or descriptions.get("back.png", "")

    # Combine descriptions into a detailed visual reference section
    visual_ref = ""
    if desc_back:
        visual_ref += f"### Card Front (Full Body Reference)\n\n{desc_back}\n\n"
    if desc_front:
        visual_ref += f"### Card Back (Detailed Portrait Reference)\n\n{desc_front}\n"

    return f"""# Image Prompt: {asset_name}

> **Style Guide**: {STYLE_GUIDE}

---

## Asset Information

- **Asset Name**: {asset_name} Portrait
- **Purpose**: Mage portrait for Heroes/Roster.md and mission briefs
- **Intended Repository Path**: `Images/Mages/{asset_name}.png`

---

## Canonical Facts

{f"### Lore\n\n{lore}\n" if lore else ""}{f"### Overview\n\n{overview}\n" if overview else ""}{f"### Ability\n\n{ability}\n" if ability else ""}{f"### Strategy Notes\n\n{strategy}\n" if strategy else ""}
---

## Reference Image Details

The following is a detailed description of the official card art for this character. Use this as a guide for the character's appearance, equipment, pose, and setting.

{visual_ref}
---

## Artistic Direction

- **Composition**: Full-body standing shot, wide environmental framing. Subject centred or slightly off-centre, facing forward or slightly angled. Gothic or ruined environment visible around them. Full figure from head to boots.
- **Mood**: Dramatic, sombre, weathered. The atmosphere of a world under siege.
- **Lighting**: Dramatic chiaroscuro — warm light from one side, cool shadow on the other. Muted, naturalistic.
- **Colour Palette**: Muted, earthy, desaturated — charcoal, deep navy, leather brown, aged metal. Small accent colours from magical effects where appropriate.
- **Art Style**: Photorealistic dark-fantasy cinematic. Like a film still, not a fantasy illustration.
- **Aspect Ratio**: 3:4 portrait.

---

## Status

- [ ] Image generated

---

## Markdown Reference

```markdown
![{asset_name}](Images/Mages/{asset_name}.png)
```
"""


def generate_nemesis_prompt(asset_name: str, descriptions: dict, data: dict | None) -> str:
    """Generate a prompt Markdown file for a nemesis."""
    lore = data.get("lore", "") if data else ""
    ability = data.get("ability", "") if data else ""
    strategy = data.get("strategy", "") if data else ""
    setup = data.get("setup", "") if data else ""
    unleash = data.get("unleash", "") if data else ""

    desc_front = descriptions.get("front.jpg", "") or descriptions.get("front.png", "")
    desc_back = descriptions.get("back.jpg", "") or descriptions.get("back.png", "")

    visual_ref = ""
    if desc_back:
        visual_ref += f"### Card Front (Full Body Reference)\n\n{desc_back}\n\n"
    if desc_front:
        visual_ref += f"### Card Back (Detailed Portrait Reference)\n\n{desc_front}\n"

    return f"""# Image Prompt: {asset_name}

> **Style Guide**: {STYLE_GUIDE}

---

## Asset Information

- **Asset Name**: {asset_name} Portrait
- **Purpose**: Nemesis portrait for World/Nemeses.md and encounter briefs
- **Intended Repository Path**: `Images/Nemeses/{asset_name}.png`

---

## Canonical Facts

{f"### Lore\n\n{lore}\n" if lore else ""}{f"### Ability\n\n{ability}\n" if ability else ""}{f"### Strategy Notes\n\n{strategy}\n" if strategy else ""}{f"### Setup\n\n{setup}\n" if setup else ""}{f"### Unleash\n\n{unleash}\n" if unleash else ""}
---

## Reference Image Details

The following is a detailed description of the official card art for this nemesis. Use this as a guide for the creature's appearance, pose, and setting.

{visual_ref}
---

## Artistic Direction

- **Composition**: Full-body standing shot, wide environmental framing. Subject centred or slightly off-centre, facing forward or slightly angled. Gothic or ruined environment visible around them. Full figure from head to boots.
- **Mood**: Threatening, ominous, oppressive. The presence of a world-ending threat.
- **Lighting**: Dramatic chiaroscuro — warm light from one side, cool shadow on the other. Muted, naturalistic.
- **Colour Palette**: Muted, earthy, desaturated — charcoal, deep navy, leather brown, aged metal. Small accent colours from magical effects where appropriate.
- **Art Style**: Photorealistic dark-fantasy cinematic. Like a film still, not a fantasy illustration.
- **Aspect Ratio**: 3:4 portrait.

---

## Status

- [ ] Image generated

---

## Markdown Reference

```markdown
![{asset_name}](Images/Nemeses/{asset_name}.png)
```
"""


def main():
    parser = argparse.ArgumentParser(
        description="Generate image prompt Markdown files from reference image descriptions."
    )
    parser.add_argument("--mage", default=None, help="Specific mage to generate a prompt for")
    parser.add_argument("--nemesis", default=None, help="Specific nemesis to generate a prompt for")
    parser.add_argument("--mages", action="store_true", help="Generate prompts for all mages")
    parser.add_argument("--nemeses", action="store_true", help="Generate prompts for all nemeses")
    parser.add_argument("--list", action="store_true", help="List what would be generated")
    parser.add_argument("--repo-root", default=None, help="Path to the repo root.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing prompt files")
    args = parser.parse_args()

    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent
    ref_root = repo_root / "AeonsEndCampaign" / "ReferenceImages"
    prompts_dir = repo_root / "AeonsEndCampaign" / "ImagePrompts"

    # Gather targets
    targets = []

    if args.mage:
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
        print("No targets found.")
        return

    if args.list:
        print(f"Would generate prompts for {len(targets)} asset(s):")
        for _, name, typ in targets:
            prompt_dir = prompts_dir / (typ + "s")
            prompt_path = prompt_dir / f"{name}.md"
            status = "EXISTS" if prompt_path.exists() else "NEW"
            print(f"  [{typ}] {name} - {status}")
        return

    generated = 0
    skipped = 0
    for asset_dir, name, typ in targets:
        # Load descriptions
        desc_path = asset_dir / "descriptions.json"
        desc_data = load_json(desc_path)
        if not desc_data or "descriptions" not in desc_data:
            print(f"SKIP: {name} — no descriptions.json found (run describe_images.py first)")
            skipped += 1
            continue

        # Load data
        data_path = asset_dir / "data.json"
        data = load_json(data_path)

        # Generate prompt content
        if typ == "Mage":
            content = generate_mage_prompt(name, desc_data["descriptions"], data)
        else:
            content = generate_nemesis_prompt(name, desc_data["descriptions"], data)

        # Write prompt file
        prompt_dir = prompts_dir / (typ + "s")
        prompt_dir.mkdir(parents=True, exist_ok=True)
        prompt_path = prompt_dir / f"{name}.md"

        if prompt_path.exists() and not args.overwrite:
            print(f"SKIP: {name} — prompt file already exists (use --overwrite to replace)")
            skipped += 1
            continue

        prompt_path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"OK:   {name} → {prompt_path.relative_to(repo_root)}")
        generated += 1

    print(f"\nDone. Generated {generated} prompt file(s), skipped {skipped}.")


if __name__ == "__main__":
    main()