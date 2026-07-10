# Aeon's End Campaign: The Whisper Below

A persistent, story-driven Aeon's End campaign for three experienced players, managed by DeepSeek V4 Pro as the Campaign Master.

## What This Is

This repository contains a complete narrative legacy campaign for the cooperative deck-building game Aeon's End. Every mission, story beat, consequence, and reward is tracked here. The campaign is designed to feel continuous — victories and defeats both shape the world.

## Owned Content

- Aeon's End (base game)
- War Eternal
- Four small expansions (names to be verified)

## How to Start a Session

1. Read `CurrentMission.md` — this is the mission you'll play.
2. Choose three mages from the four nominated.
3. Set up the game using the listed Nemesis and market.
4. Play the mission.
5. Report results using the template in `Sessions/SessionTemplate.md`.

## How to Report Results

After each game, provide:

- Mission name
- Nemesis fought
- Mages used
- Victory or defeat
- Remaining Gravehold life
- Exhausted mages
- Nemesis remaining life (if defeated by loss)
- Bonus objective result
- Killing blow (who dealt it)
- Memorable events
- Any rules questions
- Player comments

## Authoritative Files

If files conflict, this is the order of authority:

1. `CampaignState.yaml` — machine-readable canonical state
2. `CurrentMission.md` — the mission currently being played
3. `CampaignJournal.md` — human-readable narrative record
4. `World/` and `Heroes/` files — persistent lore and records
5. `Sessions/` — immutable historical records after completion

## How to Generate Images

Image prompts are created by the Campaign Master in `ImagePrompts/`. Each prompt describes exactly what the image model should generate. Generated images are stored in `Images/` and `Maps/`. Never assume an image exists until confirmed.

## Continuing With Another Model

A future Campaign Master can pick up the campaign by reading:

1. `CampaignMaster.md` — operating instructions
2. `CampaignState.yaml` — current state
3. `CurrentMission.md` — active mission
4. `CampaignJournal.md` — story so far
5. The most recent session file in `Sessions/`
6. Any relevant files in `World/` and `Heroes/`

No campaign-critical fact exists only in chat history.

## Campaign Status

- **Campaign**: The Whisper Below
- **Status**: Initialized — awaiting content verification
- **Chapter**: 1 (not yet started)
- **Sessions Played**: 0
