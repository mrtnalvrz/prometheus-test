# Creative Asset Formats — Droidscouts

This document defines the canonical file format, naming convention, and folder location for every creative asset type in this repository. All agents and contributors must follow these rules. When in doubt, the scripts are canon — see `world/canon-policy.md`.

---

## Episode Script

| Field | Value |
|---|---|
| Format | UTF-8 Markdown (`.md`) |
| Naming | `ch##-script.md` (e.g. `ch01-script.md`, `ch12-script.md`) |
| Location | `create/scripts/` |
| Template | `create/templates/chapter-script-template.md` |
| Archival PDFs | May remain in `create/scripts/` as originals; Markdown is the working copy |

**Format rules:**
- Page headers: `# PAGE [NUMBER] ([X] PANELS)`
- Panel headers: `## PANEL [NUMBER]`
- Sluglines: `**INT. or EXT. LOCATION — DAY / NIGHT / CONTINUOUS**` (always bold, always caps)
- Action lines: plain text, present tense, 1–3 lines per panel
- Captions (narration boxes): `**CAPTION:** Text`
- Character name before dialogue: `**CHARACTER NAME**` (bold, all caps)
- Parentheticals: `*(emotion or direction)*` (italic, on its own line under character name)
- Dialogue: plain text directly under character name or parenthetical
- Transitions: right-aligned at bottom of page — `CUT TO:` / `FADE OUT.` / `SMASH CUT TO:`

---

## Chapter Outline

| Field | Value |
|---|---|
| Format | UTF-8 Markdown (`.md`) |
| Naming | `ch##-outline.md` (e.g. `ch05-outline.md`) |
| Location | `create/outlines/` |
| Template | `create/templates/chapter-outline-template.md` |

**Format rules:**
- Three-act structure with scene table per act
- Each scene row includes: scene name, location, characters present, beat (what changes)
- Must include season arc threads section (Coover/Lamarr, villain structure, episode hook)
- Status field: `Concept` / `In Progress` / `Final`

---

## Character Profile

| Field | Value |
|---|---|
| Format | UTF-8 Markdown (`.md`) |
| Naming | `firstname-lastname.md` (e.g. `tony-mendoza.md`) |
| Location | `characters/profiles/` |
| Template | `characters/templates/character-profile-template.md` |

**Format rules:**
- Profile table covers: full name, age (with script citation), gender, ethnicity, parents, school/affiliation, area of expertise
- Sections: Personality, Background, Possessions, Key Story Moments, Relationships, Role in the Story, Notes
- Ages and physical details must cite the script episode that confirms them
- Any conflict with a design sheet: script is canon; note the discrepancy in the Notes section

---

## Art Direction Note (Image Companion File)

| Field | Value |
|---|---|
| Format | UTF-8 Markdown (`.md`) |
| Naming | Same base name as the image file (e.g. `Pagina_1.jpg` → `Pagina_1.md`) |
| Location | Same folder as the image it describes |
| Template | `art-direction/templates/art-direction-note-template.md` |

**Format rules:**
- Describe what the image shows in plain language
- Canon verification table: compare image details against script — flag any deviation
- Status field: `Canon-consistent` / `Has deviations` / `Needs review`
- Link to the relevant script file and character profile

---

## World / Lore Document

| Field | Value |
|---|---|
| Format | UTF-8 Markdown (`.md`) |
| Naming | Descriptive kebab-case (e.g. `villain-structure.md`, `idea-history.md`) |
| Location | `world/` or `world/[subfolder]/` |

**Format rules:**
- Must be consistent with episode scripts; note any speculative content as such
- Cross-link to relevant character profiles and canon policy

---

## Canon Hierarchy (summary)

Scripts always win. When any asset conflicts with an episode script, update the asset — not the script.

1. Episode scripts (`create/scripts/ch##-script.md`)
2. Character profiles (`characters/profiles/`)
3. World / lore documents (`world/`)
4. Comic pages (adaptation; deviations are errors)
5. Storyboards
6. Pitch materials

Full policy: `world/canon-policy.md`
