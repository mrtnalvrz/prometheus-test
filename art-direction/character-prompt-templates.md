# Droidscouts — AI Character Prompt Templates

> Copy-paste prompts for consistent AI image and video generation.
> Built for Leonardo AI, Midjourney, Kling AI, and Pika Labs.
> Always combine with the negative prompts from `art-direction/style-guide.md`.
> Character Reference image to upload is noted per character.

---

## How to Use

**For Leonardo AI (recommended):**
1. Upload the specified Character Reference JPG from `art-direction/characters/`
2. Set Character Reference weight to 0.75
3. Paste the Base Prompt
4. Add a Scene Suffix describing what the character is doing
5. Add the Standard Negative Prompt at the end

**For Kling AI / Pika (video):**
1. Generate a still image in Leonardo first
2. Use that image as the input frame in Kling/Pika
3. Add the Motion Prompt for the clip

**Standard Negative Prompt (add to every generation):**
```
photorealistic, 3D render, painterly, watercolor, grimdark, chibi,
super-deformed, blurry, low quality, extra limbs, bad anatomy,
sketch, unfinished, manga screentone, wrong hair color, aged up, aged down
```

---

## HEROES

---

### Mitchell "Mitch" Simmons

**Character Reference:** `art-direction/characters/DS__heroes_main_MitchellSimmons.jpg`
**Character Reference weight:** 0.75

**Base Prompt:**
```
Mitchell Simmons, 18-year-old African American young man, short natural black hair,
blue eyes, broad-shouldered athletic build, wearing a royal blue and orange tracksuit
with a utility belt around the waist, orange baseball cap worn backwards,
orange and blue sandal-style shoes, western comic book style, clean bold outlines,
flat cel shading, vibrant saturated colors
```

**Scene Suffixes — copy and append:**
```
// Determined / ready for action:
, standing tall with arms crossed, confident expression, slight smirk

// Using materializer:
, right hand extended, glowing orange-gold teal holographic hexagonal shapes
materializing from his palm, teal energy light on his face, dynamic action pose

// Driving TRIX-E:
, gripping a futuristic steering wheel, focused expression, interior of a
sleek dark car visible behind him, motion blur on background

// Quiet / thoughtful:
, sitting with elbows on knees, looking down, contemplative expression,
soft warm lighting
```

**Motion Prompt (Kling/Pika):**
```
Mitch raises his right hand and a teal holographic projection bursts outward
from his palm, camera slowly pulls back to reveal the full materialized construct
```

---

### Ren Zhao (Lynn Zhao)

**Character Reference:** `art-direction/characters/DS__heroes_main_RenZhao.jpg`
**Character Reference weight:** 0.75

**Base Prompt:**
```
Ren Zhao, 16-year-old Asian American teenage girl, long straight purple hair
past her shoulders, violet eyes, slim athletic build, cybernetic bionic left arm
with pink metallic plating and glowing pink-magenta energy accents,
wearing a hot pink and gold yellow sleeveless top over purple cropped leggings
and yellow sandal-style shoes, western comic book style, clean bold outlines,
flat cel shading, vibrant saturated colors
```

**Scene Suffixes:**
```
// Focused / combat ready:
, standing in a fighting stance, bionic arm raised and glowing pink,
cool determined expression, slight narrowing of violet eyes

// On her flying moped:
, riding a teal flying moped above city streets, wind blowing her purple hair back,
leaning forward confidently, speed lines on background

// Bionic arm attack:
, bionic arm extended forward, pink-magenta energy lance projecting from the hand,
dynamic low-angle shot, motion blur on the energy beam

// Calm / analytical:
, arms folded, one hand touching chin thoughtfully, slight tilt of head,
neutral composed expression
```

**Motion Prompt (Kling/Pika):**
```
Ren extends her bionic arm and a pink energy projection shoots forward,
her purple hair whips back from the force, camera follows the energy beam
```

---

### Dasha Pavlov

**Character Reference:** `art-direction/characters/DS__heroes_main_DashaPavlov.jpg`
**Character Reference weight:** 0.75

**Base Prompt:**
```
Dasha Pavlov, 13-year-old Russian teenage girl, short blonde bob haircut,
green eyes, compact athletic stocky build, wearing a green long-sleeve shirt
under a blue tactical vest, blue capri pants, and green flat shoes,
western comic book style, clean bold outlines, flat cel shading, vibrant colors
```

**Scene Suffixes:**
```
// Protective / fierce:
, standing in front of a smaller character, arms spread slightly in a protective
stance, fierce determined expression, chin slightly raised

// Flying kick:
, mid-air flying kick, leg extended, blonde hair lifting, dynamic diagonal
composition, speed lines, fierce focused expression

// Talking to Chandra:
, kneeling down to eye level with a small child, softer expression,
slight smile, protective body language

// Guarded / alert:
, back pressed against a wall, peering around a corner, tense expression,
hand raised and ready
```

**Motion Prompt (Kling/Pika):**
```
Dasha runs and launches into a flying kick, her foot connecting with an off-screen
target, camera tracks her arc through the air in slow motion
```

---

### Marty Mendoza

**Character Reference:** `art-direction/characters/DS__heroes_main_MartyMendoza.jpg`
**Character Reference weight:** 0.75

**Base Prompt:**
```
Marty Mendoza, 15-year-old Latin American teenage boy, dark blue hair,
dark blue eyes, thick red rectangular glasses, lanky build, wearing a red hoodie
with teal sleeve accents, dark navy pants, and red and teal sandal-style shoes,
western comic book style, clean bold outlines, flat cel shading, vibrant colors
```

**Scene Suffixes:**
```
// Hacking / laptop:
, hunched over a laptop with a frog insignia sticker, green code reflected
in his glasses, concentrated expression, one hand typing rapidly

// Annoyed / guarded:
, arms crossed, slight frown, eyes narrowed, skeptical expression,
looking sideways at something off-panel

// Surprised / rare smile:
, glasses slightly pushed up nose, genuine wide smile, surprised eyebrows raised,
warm lighting on face

// Holographic call:
, holding a small glowing device, teal holographic display in front of him,
speaking urgently, one hand gesturing

// Using Trixie AI:
, speaking into a wrist device, teal holographic avatar visible nearby,
serious focused expression
```

**Motion Prompt (Kling/Pika):**
```
Marty pushes his glasses up with one finger and turns to look directly at camera,
slight smirk forming, teal holographic data streams visible around him
```

**Splash Page Prompt** *(tested — use this for action/hero splash pages)*
> Based on `Marty_Splash_prop1.png`. Energy color corrected to teal. Style anchored to western comic.
```
dynamic comic book splash page, western comic book style with anime-influenced
character design, bold ink outlines, flat cel shading, vibrant saturated colors,
dramatic action pose, speed lines background,
Latino teenage boy 15 years old, dark navy spiky hair, red thick-framed glasses,
red hoodie with teal sleeve accents, dark navy pants, red and teal shoes,
running forward toward camera, both hands crackling with teal holographic energy
and glowing cyan data streams, green code fragments and hacker UI text exploding
outward, low angle heroic perspective, cinematic lighting with teal rim light,
dark city background with neon reflections
```
> Negative: `red energy, pink energy, villain colors, photorealistic, 3D render, chibi, bad anatomy`

---

### Tony Mendoza (Anthony)

**Character Reference:** `art-direction/characters/DS__heroes_main_TonyMendoza.jpg`
**Character Reference weight:** 0.70

> ⚠️ IMPORTANT: The design sheet shows dark brown hair. Canon is **RED hair**.
> Always specify red hair explicitly. Do not use the reference without overriding hair color.

**Base Prompt:**
```
Tony Mendoza, 13-year-old Latin American boy, short spiky red hair,
brown eyes, energetic compact build, wearing an orange and green color-block vest
over a green short-sleeve shirt, brown cargo shorts, and orange and green shoes,
western comic book style, clean bold outlines, flat cel shading, vibrant colors,
red spiky hair
```

**Scene Suffixes:**
```
// Excited / enthusiastic:
, wide grin, arms raised or pumping fist, eyebrows up, bouncing energy in pose

// Worried about mom:
, eyebrows furrowed, eyes wide and glistening, hands clasped together,
lower lip slightly forward, earnest expression

// Running:
, sprinting at full speed, red hair streaming back, arms pumping,
dynamic low-angle shot, speed lines

// Operating a drone:
, looking up and pointing at something above, small drone device in other hand
glowing green, excited expression
```

**Motion Prompt (Kling/Pika):**
```
Tony pumps his fist in the air and spins around, red hair catching the light,
huge grin on his face, camera rotates around him in a 180-degree arc
```

---

### Chandra Kalam

**Character Reference:** None (PDF design sheet only — no usable JPG)
> Upload `art-direction/characters/chandra.pdf` pages as reference if your tool accepts PDF,
> or use text-only prompting until a JPG reference is created.

**Base Prompt:**
```
Chandra Kalam, 9-year-old Indian girl, black hair in pigtails or two buns,
dark brown eyes, small round-faced child proportions, wearing a colorful
casual outfit appropriate for a 9-year-old, often carrying a stuffed dragon toy
(BiBi — small purple dragon plushie) or accompanied by a small wheeled robot (Robi),
western comic book style, clean bold outlines, flat cel shading, vibrant colors,
child proportions, noticeably smaller than the teenage characters
```

**Scene Suffixes:**
```
// With BiBi:
, hugging a small purple stuffed dragon toy to her chest, content expression,
wide curious eyes

// Wonder / discovery:
, eyes wide, mouth slightly open in amazement, both hands raised,
looking up at something large and impressive off-panel

// With Robi (R081):
, standing next to a small wheeled robot with a red "R" painted on it,
hand resting on the robot affectionately, cheerful expression

// Brave / determined:
, chin raised, small fists clenched at sides, eyes set with unusual seriousness
for a 9-year-old, facing something much larger
```

**Motion Prompt (Kling/Pika):**
```
Chandra holds up her stuffed dragon BiBi and waves its arm at Robi the robot,
who blinks its lights in response, camera slowly zooms in on the pair
```

---

## ALLIES

---

### Dr. Maria Mendoza

**Character Reference:** `art-direction/comic-prototype/Colored Comic/DS_volume1_pag07.jpg`
*(Use as Style Reference, not Character Reference — crop the panel showing her face/torso)*
**No standalone design sheet exists.**

**Base Prompt:**
```
Dr. Maria Mendoza, adult woman in her late 30s to early 40s, dark navy blue hair
worn up or in a loose style, medium-brown skin, brown eyes, strong confident
presence, wearing a white form-fitting IDEA institute suit with a small silver
logo on the chest, professional and authoritative posture,
western comic book style, clean bold outlines, flat cel shading, vibrant colors
```

**Scene Suffixes:**
```
// Leading the IDEA team:
, raising a champagne glass in a toast, warm smile, scientist colleagues visible
in background, celebration setting

// Fighting / defiant:
, holding a small device pointed forward, teal energy net shooting from it,
fierce expression, hair slightly disheveled

// Captured / defiant:
, wrists held, chin raised defiantly, dark eyes blazing with resistance,
refusing to show fear despite the situation

// Tender / maternal:
, eyes soft, slight smile, looking toward her sons with quiet love
```

---

### Helen (H.E.L.E.N)

**Character Reference:** None — no design sheet exists. Text-only prompting required.

**Base Prompt:**
```
Helen, holographic AI woman, chrome silver semi-transparent glowing form,
female figure rendered entirely in cool teal and white holographic light,
slightly luminous and translucent at the edges, elegant composed posture,
calm and intelligent expression, projected from a floating chrome orb nearby,
teal energy aura surrounding her, futuristic holographic aesthetic,
western comic book style, clean outlines, flat cel shading, teal and white palette
```

**Scene Suffixes:**
```
// First appearance / awakening:
, slowly materializing in a dark lab, flickering slightly as she stabilizes,
soft teal glow illuminating the surrounding equipment, calm welcoming expression

// Helping the kids:
, gesturing with one hand toward a holographic display of lab schematics,
the floating projection orb visible nearby, instructive expression

// Serious / concerned:
, arms at sides, expression unreadable, slight narrowing of eyes,
inner teal light slightly brighter as if processing something important
```

---

## VILLAINS

---

### Dr. Garoussen (Elroy Garoussen / "Le Loup")

**Character Reference:** `art-direction/characters/DS__villians_antagonist_DrGaroussen.jpg`
**Character Reference weight:** 0.80

**Base Prompt:**
```
Dr. Garoussen, tall lean older man approximately 60-70 years old, slicked-back
white-grey hair, pale skin, red cybernetic eye on the right side replacing the
natural eye with a glowing red-pink bionic implant, metal cybernetic chin implant,
cold contemptuous expression, wearing a dark navy military-style long coat
with a red diagonal sash across the chest, black trousers and shoes,
imposing authoritative posture, western comic book style, clean bold outlines,
flat cel shading, dark color palette with red accent
```

**Scene Suffixes:**
```
// Imposing / commanding:
, standing with hands clasped behind his back, chin slightly raised, cold stare,
dark corridor background, his cybernetic eye glowing red in the shadows

// Threatening / close-up:
, extreme close-up on face, cybernetic eye pulsing red-pink, thin cold smile,
very low key lighting with red rim light from the eye

// Striking a subordinate:
, hand extended in mid-strike, motion blur, contemptuous expression,
a suited figure flying backward in background

// Reporting to Master:
, speaking into a wrist communicator, one hand behind back, serious expression,
dark environment
```

**Motion Prompt (Kling/Pika):**
```
Garoussen slowly turns to face camera, his red cybernetic eye pulses once,
and a thin cold smile forms, camera slowly pushes in on his face
```

---

### Dark Agents (Template)

**Character Reference:** `art-direction/characters/DS__villians_extras_darkagents.jpg`
**Character Reference weight:** 0.65

**Base Prompt:**
```
dark agent villain henchman, tall imposing figure 185-200cm, dark charcoal
business suit, white shirt, dark tie, distinctive bright pink-red visor
sunglasses obscuring the eyes, small lightning bolt symbol on left lapel,
neutral threatening expression, broad shouldered, western comic book style,
clean bold outlines, flat cel shading
```

> Note: Hair and skin color may vary. The visor glasses are the non-negotiable identifier.

**Scene Suffixes:**
```
// Group / squad:
, three dark agents standing in a line, identical posture, visors glowing faintly,
intimidating formation

// Firing energy weapon:
, arm extended forward, bright pink-magenta energy blast shooting from a small
handheld weapon, "ZINNG" sound effect text nearby, action pose

// Crashed / defeated:
, lying on floor wrapped in teal energy restraints, visor cracked,
suit disheveled
```

---

## EXTRAS

---

### IDEA Scientists (Template)

**Character Reference:** `art-direction/characters/DS__neutral_extras_scientists.jpg`
**Character Reference weight:** 0.60

**Base Prompt:**
```
IDEA institute scientist, wearing a white lab coat with teal IDEA logo on the back,
professional attire underneath, carrying a blue data tablet,
diverse background character, neutral setting of a modern high-tech laboratory,
western comic book style, clean outlines, flat cel shading
```

---

## Shared Scene Prompts

These are full prompts for common multi-character scenes.

### The Team Together (heroes assembled)
```
Droidscouts team assembled, six diverse teenagers and a young adult, Mitchell Simmons
18-year-old African American in blue orange tracksuit, Ren Zhao 16-year-old Asian
American with purple hair and bionic arm in pink yellow outfit, Dasha Pavlov 13-year-old
Russian blonde in green and blue tactical outfit, Marty Mendoza 15-year-old Latino
with blue hair and red glasses in red hoodie, Tony Mendoza 13-year-old Latino with
red spiky hair in orange green vest, Chandra Kalam 9-year-old Indian girl in colorful
outfit holding stuffed dragon, dynamic group shot, each character in a distinct pose
showing their personality, underground futuristic lab background, teal ambient lighting,
western comic book style, flat cel shading, vibrant colors, clean outlines,
professional comic book illustration
```

### IDEA Raid Opening (villain attack)
```
IDEA institute hallway under attack, scientists in white lab coats fleeing in panic,
dark agent henchmen in black suits with pink visor glasses advancing through smoke,
emergency red lighting, chaos and motion blur, dramatic diagonal composition,
western comic book style, flat cel shading, high contrast, pink-magenta energy
weapon glow, professional comic book illustration
```

### Compound 59 First Entry
```
children entering a massive underground laboratory for the first time, enormous
circular chamber with amber lighting slowly flickering on, advanced robotics and
machinery visible in background, teal holographic displays activating on walls,
characters small against the vast scale of the space, wonder and awe on their faces,
western comic book style, flat cel shading, warm amber and teal color palette
```
