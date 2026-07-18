# Campaign Art Style Guide

Every image in this campaign must match the following style.

---

## Style

Cinematic dark-fantasy realism — photorealistic high-end fantasy game cinematic.

## Core Description

Grounded medieval Gothic setting, mature naturalistic character design, realistic ageing and skin texture, weathered layered fabrics and tarnished metal, restrained practical costume, dramatic chiaroscuro lighting, warm candlelight against cool ambient shadows, muted charcoal and earthy colour palette, subtle atmospheric haze, shallow depth of field, highly detailed face, tactile materials, sombre dignified mood, natural proportions, realistic film colour grading, 85mm portrait photography, subtle film grain, sharp facial focus, softly blurred Gothic background.

## Reusable Style Block

Use this as the core style block in every image prompt:

> Cinematic dark-fantasy realism, photorealistic high-end fantasy game cinematic, grounded medieval Gothic setting, mature naturalistic character design, realistic ageing and skin texture, weathered layered fabrics and tarnished metal, restrained practical costume, dramatic chiaroscuro lighting, warm candlelight against cool ambient shadows, muted charcoal and earthy colour palette, subtle atmospheric haze, shallow depth of field, highly detailed face, tactile materials, sombre dignified mood, natural proportions, realistic film colour grading, 85mm portrait photography, subtle film grain, sharp facial focus, softly blurred Gothic background.

## Palette

- Muted earth tones
- Charcoal black
- Weathered navy
- Dark brown
- Tarnished bronze
- Candlelight amber
- Slate grey
- Weathered stone
- No saturated colours

## Lighting

- Dramatic chiaroscuro (Rembrandt-style)
- Warm candlelight against cool shadows
- Natural, overcast skies for exteriors
- Warm torchlight indoors
- Subtle atmospheric haze

## Avoid

- Anime
- Steampunk, brass machinery, gears, goggles, pipes, Victorian industrial
- Comic book style, concept art, cartoon
- Obvious digital painting, visible brush strokes
- Glossy plastic skin, beauty retouching, fashion photography
- Glowing runes, neon lighting, colourful magic effects
- Exaggerated armour, oversized pauldrons, ornate crown, sexualised costume
- Heroic pose, smiling, perfect symmetry, young-looking face
- Saturated colours, clean new clothing, bright daylight, flat lighting
- 3D render look, video game UI
- Low-detail background, generic fantasy illustration

## Negative Prompt

steampunk, brass machinery, gears, goggles, pipes, Victorian industrial design, excessive ornamentation, glowing runes, neon lighting, colourful magic effects, anime, comic book style, obvious digital painting, visible brush strokes, glossy plastic skin, beauty retouching, fashion photography, perfect symmetry, young-looking face, exaggerated armour, oversized pauldrons, ornate crown, sexualised costume, heroic pose, smiling, saturated colours, clean new clothing, bright daylight, flat lighting, generic fantasy illustration, cartoon, concept sketch, low-detail background

## Overall Feeling

A grounded, mature medieval Gothic world — tactile, weathered, sombre, and cinematic. Like a film still or high-end game cinematic, not a fantasy illustration.

---

## Usage

All image prompts in `ImagePrompts/` must reference this guide. The `generate_images.py` script automatically appends these style constraints to every prompt.