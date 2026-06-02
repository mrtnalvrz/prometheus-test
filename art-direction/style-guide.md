# Droidscouts — Visual Style Guide

> This document is the canonical reference for all AI-generated and human-produced artwork.
> When any generated image conflicts with this guide, regenerate — do not adapt the guide to the output.
> Canon source: `world/canon-policy.md`

---

## 1. Overall Art Style

**Style:** Western comic book with anime-influenced character design.

Droidscouts sits between a North American superhero comic and a Japanese animated series. Characters are expressive and slightly stylized (large eyes, clean silhouettes, dynamic poses) but grounded enough to read as real people in a believable near-future world. It is not chibi. It is not hyper-realistic. It occupies the visual space of shows like *Big Hero 6*, *Spider-Man: Into the Spider-Verse*, and *Invincible* (Season 1 tone — adventure first, drama second).

**Key visual qualities:**
- **Clean, confident outlines** — bold black lines, no scratchy or painterly edges
- **Flat cel shading** — colors are solid with 1–2 levels of shadow, not gradient-heavy
- **High contrast** — backgrounds and environments use deeper, moodier tones; characters pop with brighter, saturated colors
- **Dynamic but readable** — action panels are energetic but always legible; the reader always knows who is where

**What it is NOT:**
- Not photorealistic or 3D-rendered
- Not watercolor or painterly
- Not dark/gritty (the tone is adventurous; darkness is used for villain scenes, not as a default)
- Not overly comedic or chibi-deformed

---

## 2. Color Language

This is the most important rule in the visual system. Colors signal faction.

### Hero / Mendoza Technology
- **Primary:** Teal / Cyan (`#00BCD4` / `#26C6DA`)
- **Secondary:** Orange-gold (`#FF8C00`) — materializer device glow
- Used for: materializer projections, holographic displays, energy nets, friendly tech UI

### Villain / Dark Agent Technology
- **Primary:** Pink-Magenta (`#FF1493` / `#E91E8C`)
- **Secondary:** Deep red (`#C62828`) — cybernetic eye, targeting systems
- Used for: energy weapons (SPEOW/ZINNG blasts), Garoussen's eye, ELIMINATE UI, villain targeting

### IDEA Institution
- **Primary:** Teal (`#00BCD4`) + White
- **Secondary:** Light grey (`#ECEFF1`)
- Used for: lab coats, IDEA branding, interior environments

### Neutral / World
- City: Cool blue-grey tones (`#546E7A`, `#78909C`)
- School: Warm neutral (`#F5F0E8`, warm concrete)
- Desert: Warm sand and ochre (`#C19A6B`, `#E8D5A3`)
- Compound 59: Darker teal-grey interior with amber accent lighting (warmer than IDEA — it's older, more lived-in)

### Color Rule Summary
> If it glows teal → heroes. If it glows pink/magenta → villains. Never swap.

---

## 3. Character Design Principles

### Silhouette
Every main character must be recognizable by silhouette alone. Key identifiers:
- **Mitch** — orange cap, large frame, utility belt
- **Ren** — long purple hair, bionic left arm
- **Dasha** — short blonde bob, stocky/athletic build, tactical vest
- **Marty** — glasses, hoodie, slightly hunched (always near a laptop)
- **Tony** — red spiky hair, energetic posture, smaller than Marty
- **Chandra** — tiny, pigtails, always with BiBi or Robi nearby
- **Garoussen** — tall, gaunt, red eye, swept-back white hair, diagonal red sash

### Age Reads
Characters must read as their canonical age at a glance:
- Chandra (9) — noticeably smaller than the others, round face, child proportions
- Tony (13) — energetic preteen, shorter than Marty
- Dasha / Tony (13) — similar age, clear difference in build and personality
- Marty (15) — lanky teen, not yet filled out
- Ren (16) — teenager but more composed, taller than Dasha/Tony
- Mitch (18) — clearly older than the kids; broader shoulders, more adult face

### Expressions
Characters should have a wide expression range. Their emotional default:
- **Mitch** — calm confidence; rarely panics
- **Ren** — focused and cool; smiles are quiet and rare
- **Dasha** — direct and fierce; default expression is determined, not angry
- **Marty** — guarded; slight frown is resting face; genuine smiles are earned
- **Tony** — wide open; eyebrows always expressive; default is upbeat
- **Chandra** — wonder and delight; rarely afraid, usually curious
- **Garoussen** — cold; contempt rather than anger; smiles are unsettling

---

## 4. Environment Design

### IDEA Headquarters
- Interior: Cool blue-grey walls, teal accent lighting strips, clean glass and metal
- Feeling: Corporate-modern, impressive, slightly sterile
- Dominant colors: White, light grey, teal
- Key elements: Wall-spanning monitor arrays, open lab benches, IDEA logos on all surfaces

### Compound 59 / ERCHIn (Underground Lab)
- Interior: Darker, more aged than IDEA — teal-grey metal, amber work lighting
- Feeling: Hidden, powerful, slightly mysterious — not abandoned, more like a sleeping giant
- Key elements: Circular central hub, tram system, factory wing, robotics bay, hidden chrome elevator
- The lab is massive — panels should emphasize scale when the kids first arrive

### St. Newton Academy
- Exterior: Modern school, warm concrete and glass, trees, open campus
- Interior: Standard school — classrooms, lockers, courtyard with benches
- Feeling: Normal suburban world before everything changes

### The City
- Aesthetic: Near-future — flying vehicles, holographic billboards, mix of old and new architecture
- IDEA tower is the dominant landmark — visible from most city angles
- Color: Cool blues and silvers at night; warmer in daylight

### The Desert (Compound 59 approach)
- Wide, empty, and dramatic — mountains in the far distance
- No visible entrance to the lab — the chrome elevator rises from a featureless flat area
- Color: Warm sand, ochre, dusty sky

---

## 5. Lighting and Mood

### Default (adventure scenes)
- Bright, even lighting — no heavy shadows
- Warm fill light, cool rim light

### Action sequences
- High contrast — strong directional light, dramatic shadows
- Energy weapon glow provides colored secondary lighting (teal or magenta)

### Villain scenes
- Cooler, more desaturated base — the color comes from their energy tech (magenta/red)
- Garoussen's cybernetic eye provides a red rim light on his face in close-ups

### Compound 59 first entry
- Amber/warm — the lab waking up for the first time; lights flickering on
- Helen's projection adds a soft teal glow to the environment

### Emotional/quiet scenes
- Softer, warmer lighting — slightly lower contrast
- Often a single dominant light source (lamp, screen glow, window)

---

## 6. AI Generation Guidelines

### Positive style prompts (use these in every generation)
```
western comic book style, anime-influenced character design, clean bold outlines,
flat cel shading, vibrant saturated colors, dynamic pose, high contrast,
professional comic book illustration, white background or scene-appropriate background
```

### Negative prompts (always add these)
```
photorealistic, 3D render, painterly, watercolor, dark and gritty, grimdark,
chibi, super-deformed, blurry, low quality, extra limbs, bad anatomy,
sketch, rough, unfinished, manga screentone
```

### For character reference uploads (Leonardo AI / similar tools)
- Upload the NIBIN design sheet JPG as the primary Character Reference
- Set character reference weight to 0.7–0.85 (too high = stiff, too low = drifts)
- Always specify the character name and age in the prompt
- Specify the scene/emotion before describing the character

### For panel generation
Structure prompts as:
```
[scene description], [character name] [doing what], [emotional beat],
[camera angle], western comic book style, flat cel shading, clean outlines,
vibrant colors, [lighting note if special]
```

### Camera angles that work well for each scene type
- **Establishing shot:** Wide, slight high angle — shows environment scale
- **Dialogue:** Medium shot, slight low angle — makes characters feel present
- **Action:** Low angle or Dutch tilt — dynamic energy
- **Character close-up:** Eye level — emotional connection
- **Villain reveal:** Slightly low angle, slightly tilted — imposing

---

## 7. Reference Files in This Repository

| Asset | Location | Use for |
|---|---|---|
| Mitchell Simmons design sheet | `art-direction/characters/DS__heroes_main_MitchellSimmons.jpg` | Character Reference upload |
| Ren Zhao design sheet | `art-direction/characters/DS__heroes_main_RenZhao.jpg` | Character Reference upload |
| Dasha Pavlov design sheet | `art-direction/characters/DS__heroes_main_DashaPavlov.jpg` | Character Reference upload |
| Marty Mendoza design sheet | `art-direction/characters/DS__heroes_main_MartyMendoza.jpg` | Character Reference upload |
| Tony Mendoza design sheet | `art-direction/characters/DS__heroes_main_TonyMendoza.jpg` | Character Reference upload — **note: hair must be RED, not brown as shown** |
| Dr. Garoussen design sheet | `art-direction/characters/DS__villians_antagonist_DrGaroussen.jpg` | Character Reference upload |
| Colored page E1 (best style ref) | `art-direction/comic-prototype/Colored Comic/DS_volume1_pag07.jpg` | Style Reference for tone/palette |
| Dark agents template | `art-direction/characters/DS__villians_extras_darkagents.jpg` | Character Reference upload |
| IDEA scientists template | `art-direction/characters/DS__neutral_extras_scientists.jpg` | Background character reference |

---

## 8. What's Still Missing (flag for future sessions)

- Chandra Kalam standalone JPG reference (PDF only; needs conversion or new illustration)
- Dr. Maria Mendoza standalone design sheet (visual established in colored pages but no turnaround)
- Helen design sheet (described in scripts; no visual reference exists yet)
- Environment/location design sheets for all major settings
- Character expression sheets (6 emotions minimum per main character)
