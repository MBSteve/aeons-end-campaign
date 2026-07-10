# Images

This directory contains all generated image assets for the campaign.

---

## Directory Structure

Images are organized by category:

```text
Images/
├── NPCs/           # Character portraits
├── Relics/         # Relic illustrations
├── Chapters/       # Chapter splash art
├── Scenes/         # Major story-scene illustrations
└── Locations/      # Location illustrations
```

Subdirectories will be created as needed when images are generated.

---

## Current Images

*No images have been generated yet.*

---

## Image Generation Workflow

1. Campaign Master creates a prompt in `ImagePrompts/`
2. Image model generates the image
3. User confirms the image exists
4. Image is saved in the appropriate subdirectory
5. Campaign Master updates relevant campaign files with the image reference

The Campaign Master must never assume an image exists before confirmation.
