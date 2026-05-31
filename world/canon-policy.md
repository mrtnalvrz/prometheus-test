# Canon Policy

## Source of Truth Hierarchy

**Scripts are always canon.** When any other asset (comic pages, storyboards, pitch materials, character sheets, or lore documents) conflicts with a script, the script wins. All other assets must be corrected to match the script, not the other way around.

| Priority | Asset | Notes |
|---|---|---|
| 1 — Canon | Episode scripts (`season-1/scripts/`) | Definitive source for all story events, dialogue, character behavior, and world details |
| 2 — Reference | Character profiles (`characters/profiles/`) | Must reflect what the scripts establish |
| 3 — Reference | World documents (`world/`) | Must reflect what the scripts establish |
| 4 — Production | Comic pages (`art-direction/comic-prototype/`) | Adaptation of scripts; any deviation is an error to be corrected |
| 5 — Production | Storyboards (`season-1/storyboards/`) | Visual planning; subordinate to script |
| 6 — Marketing | Pitch materials (`pitch/`) | Summary of the project; may lag canon during active development |

## How to Handle Conflicts

- If a comic page shows something that contradicts a script, mark it with a note in the companion `.md` file and flag it for correction in the next art revision.
- If a character profile or world document contradicts a script, update the document immediately — do not leave conflicting canon in reference files.
- If a script contradicts itself across episodes, flag the conflict in `Final-Productization-Checklist.md` for author review. Do not resolve script-vs-script conflicts without explicit author direction.

## For Agents

When populating or updating any reference document from source material, always check the scripts first. If the scripts have not been converted to Markdown and are only available as PDFs, note any unverified claims with `*(unverified — check script PDF)*` until they can be confirmed.
