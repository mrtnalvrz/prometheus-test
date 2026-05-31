# Droidscouts
> **Creative Production Repository — Comic Series Workflow**

*Working title. Series title subject to change.*

---

## Project Description

**Droidscouts** is a robotics-themed comic book series fifteen years in development, originally conceived as an educational tool for teaching children about robotics and programming. It has grown into a full science-fiction action series with deep lore, an ensemble cast, and a multi-season arc currently targeting completion of Season 1.

### The World

An alternative version of Earth where technology has become the defining divide between those who have and those who don't. Governments are largely controlled by corporations that are depleting the planet's resources. For some this world is a Utopia; for others, a Dystopia.

### Season 1 Premise

A group of young prodigies — ranging in age from 7–8 to 15–16 — are thrown together when a mysterious enemy kidnaps their genius parents. Each kid brings a different area of expertise: Robotics, Computer Sciences, Genetics, and Mechanics. To fight back, they take command of the secret resources their parents left behind: a fully automated laboratory, gear capable of materializing instruments and robots on demand, and a highly sophisticated AI named **Helen**.

Season 1 opens as a straightforward teenage action-adventure but escalates through progressively darker plot threads toward the finale. The arc spans 10–12 chapters.

---

## This Repository

This repository is the canonical creative production workspace for Droidscouts. It versions and tracks all core creative assets, and uses a quality-controlled, agent-ready governance system to keep contributors — human and AI — working from the same state.

**Asset types managed here:**

- **Issue scripts** — scene-by-scene panel scripts for each chapter
- **Character and lore bibles** — reference documents for characters, factions, world rules, and Helen's AI profile
- **Story arc outlines** — season- and chapter-level plot structure
- **Art direction notes** — visual style guides, panel layout conventions, and design references
- **Pitch materials** — series bible and pitch documents

---

## Repository Map

| Path | Contents |
|---|---|
| `season-1/` | Chapter-by-chapter scripts, outlines, and the Season 1 chapter tracker |
| `characters/` | Character profiles, relationship maps, and voice/design reference |
| `world/` | World-building docs, lore, factions, and technology canon |
| `art-direction/` | Visual style guides, panel layout conventions, and design reference |
| `pitch/` | Series pitch and series bible |
| `scripts/` | Automation entry points and quality/workflow utilities |
| `context/prompts/` | Reusable prompts for agent-driven workflow tasks |
| `docs/` | Contributor documentation, onboarding, and workflow guides |
| `Final-Productization-Checklist.md` | Open, actionable backlog for all unresolved creative and tooling work |
| `Final-Optimization-Checklist.md` | Tracking for tests exceeding the 0.20s latency budget |

> **Note:** `season-1/`, `characters/`, `world/`, `art-direction/`, and `pitch/` are planned folders to be created as part of the initial creative asset migration. See `Final-Productization-Checklist.md` for the setup tasks.

---

## Getting Started

1. Create and activate a virtual environment.
2. Install dev dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

3. Run the required wrappers before any commit:

```bash
python scripts/run_precommit_suite.py
python scripts/run_tests.py
```

---

## Contributor and Agent Policy

- Read `AGENTS.md` before making any changes.
- Process `Final-Productization-Checklist.md` in dependency order — prerequisites first.
- Use only the wrapper commands above for quality and testing. Never invoke hooks or pytest directly.
- Surface unresolved work in `Final-Productization-Checklist.md` using the entry template (Scope, Target Files, Dependencies, DONE WHEN).

---

## Checklist Policy

- `Final-Productization-Checklist.md` stores all open, actionable work — creative, tooling, and documentation. Remove entries when complete; rewrite partial work as remaining scope only.
- `Final-Optimization-Checklist.md` governs tests exceeding the 0.20s latency budget, with separate sections for pending audits and confirmed justified exceptions.
- The `✅` marker in `Final-Optimization-Checklist.md` is reserved for confirmed exceptions backed by a completed test-level code audit.

---

## Timestamp and UTF-8 Policy

- Save all repository text assets as UTF-8.
- Derive dates and timestamps from Git metadata or other trusted sources — never from model-internal clocks.
- When documenting execution timelines, use explicit absolute dates from trusted sources.
