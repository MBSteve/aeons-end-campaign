"""Re-test Adelheim with full-body composition + reference images"""
import sys, json, base64, os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_images import API_KEY, STYLE_GUIDE_CONSTRAINTS, build_image_prompt, parse_prompt_file, generate_image

prompt_file = Path(__file__).resolve().parent.parent / "AeonsEndCampaign" / "ImagePrompts" / "Adelheim.md"
ref_dir = Path(__file__).resolve().parent.parent / "AeonsEndCampaign" / "ReferenceImages" / "Mages" / "Adelheim"

fields = parse_prompt_file(str(prompt_file))
base_prompt = build_image_prompt(fields)

# Test: Text + Reference Images with updated composition
print("\n=== TEST C: Full-body prompt + Reference Images ===")
ref_imgs = [ref_dir / "front.jpg", ref_dir / "back.jpg"]
existing = [p for p in ref_imgs if p.exists()]
print(f"  Using references: {[p.name for p in existing]}")

ref_prompt = base_prompt + "\n\nIMPORTANT: Use the attached reference images as a guide for the character's overall silhouette, equipment, and colour palette. However, reimagine the art style into cinematic dark-fantasy realism — do NOT copy the card's illustration style."
img = generate_image(ref_prompt, API_KEY, reference_images=existing)
if img:
    Path("adelheim_test_C_fullbody_with_ref.png").write_bytes(img)
    print("  Saved: adelheim_test_C_fullbody_with_ref.png")