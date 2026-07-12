"""Test D: Minimal prompt — just recreate the person from reference images"""
import sys, json, base64, os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_images import API_KEY, STYLE_GUIDE_CONSTRAINTS, generate_image

ref_dir = Path(__file__).resolve().parent.parent / "AeonsEndCampaign" / "ReferenceImages" / "Mages" / "Adelheim"
existing = [p for p in [ref_dir / "front.jpg", ref_dir / "back.jpg"] if p.exists()]

print("\n=== TEST D: Minimal prompt + Reference Images ===")
print(f"  Using references: {[p.name for p in existing]}")

# Minimal prompt — just describe the person and let reference images do the work
minimal_prompt = (
    "Recreate this character as a cinematic dark-fantasy realism portrait. "
    "Full-body standing shot showing head to boots. "
    "The character is an older bald man with a white beard, wearing practical breach mage attire — "
    "a dark coat, weathered fabrics, subtle violet crystal accents. "
    "He stands in a Gothic stone chamber, calm and composed, looking slightly to the left. "
    "Atmospheric lighting, muted earthy colours, photorealistic style.\n\n"
    f"{STYLE_GUIDE_CONSTRAINTS}"
)

print(f"  Prompt ({len(minimal_prompt)} chars)")
img = generate_image(minimal_prompt, API_KEY, reference_images=existing)
if img:
    Path("adelheim_test_D_minimal_with_ref.png").write_bytes(img)
    print("  Saved: adelheim_test_D_minimal_with_ref.png")