# Maps

This directory contains versioned map assets for the campaign.

---

## Naming Convention

Maps are versioned to track changes over time:

```text
World_v1.png
World_v2.png
World_v3.png
Gravehold_Region_v1.png
Gravehold_Region_v2.png
```

The Campaign Master should never assume a map exists until the user confirms it has been generated.

---

## Current Maps

*No maps have been generated yet.*

---

## Map Generation Workflow

1. Campaign Master creates a prompt in `ImagePrompts/`
2. Image model generates the map
3. User confirms the map exists
4. Map is saved here with appropriate version number
5. Campaign Master updates relevant campaign files with the map reference
