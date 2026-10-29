---
name: web-design-reference-miner
description: Find and vet design references for a build brief, then append them to the shared Goliath reference library via the append script. Use when the design-reference-library is thin for a brief, or when expanding the library. Built by Goliath Marketing (goliathmarketing.io).
version: 1.0.0
author: Goliath Marketing
license: MIT
tags: [web-design, references, research, ui, landing-page, design-gallery, mining]
platforms: [linux, macos, windows]
triggers:
  - find design references
  - mine design inspiration
  - expand the reference library
  - find references for a section
  - out of geo competitor reference
  - reference mining
---

# Web Design Reference Miner

Finds and vets design references for a build brief and adds them to the shared
Goliath reference library. Use this only two ways: when a build needs a section
type the library doesn't cover well, or as a maintenance pass to grow the
library. Browsing galleries is expensive, so this runs on demand or as a
batched maintenance job — never as part of every build.

## Where the library lives

- Repo: `goliathmarketing89/agentic-web-design` (GitHub)
- Library file: `references/design-reference-library.md`
- Contract: `references/reference-spec.md` — READ THIS FIRST
- Append script: `references/append_reference.py`

Clone the repo (or pull the latest) before mining. The library is the single
source of truth: **never hand-edit it. Append through the script.** The spec
and script enforce the entry format so any agent's additions land the same way.

## The rule that governs every find

Two independent scores on every entry — **conv** (does it convert) and **wow**
(does it impress). Awwwards-style sites are frequently art-over-conversion. An
entry only makes the library if it converts well, OR it wows *and* has one
concrete thing worth lifting. No vague praise, no "unreviewed" bucket. Vetted
or it's not in.

## The two search modes

### 1. Out-of-geography competitors (start here for client work)

The client is a Detroit plumber. Do NOT mine Detroit plumbers — that's their
direct competitive field. Instead pull the same vertical in a different market:

- A different full market (LA, Austin, Toronto plumbers).
- Award-winning or flagship sites in the vertical.
- Marketing-blog roundups: "<vertical> best websites 2025", "<vertical> web
  design awards".

Why it works: same industry, no conflict, and those pages are usually
conversion-optimized because they compete on leads in their own market.

Mark these `source: out-of-geo`.

### 2. Design galleries (for the wow layer)

Only when the brief needs the site to *impress* as well as convert:

- awwwards.com, cssdesignawards.com (art-forward — score `conv` honestly low
  unless it actually sells)
- land-book.com, landings.dev, refero.design, minimal.gallery, supahero.io
  (hero sections), cta.gallery (CTAs), pageflows.com (app flows)

Mark these `source: gallery`.

## The workflow

1. **Pull the newest library.** `git -C <repo> pull` so you're not duplicating
   entries already logged.

2. **Check what's already there for the brief before you browse.**
   `python3 references/append_reference.py --dry-run` won't help here — instead
   grep the library for the section type and vertical:
   `grep -A6 "## <type>" references/design-reference-library.md`. If it already
   covers the brief well, STOP. Recommend the existing entries, don't re-mine.

3. **Browse for new candidates** using the search mode that fits (see above).
   For each candidate that might cut it, open the page and check:

   - Does it actually convert, or is it just pretty? (Look: is there a clear
     CTA above the fold? Trust signals near the action? A single job?)
   - What ONE element is worth lifting? Be specific: "massive layered headline,
     no card, phone visible above fold" — not "nice layout".
   - Which section type is it (see taxonomy in reference-spec.md)?

4. **Build the JSON payload.** One object per accepted entry. Required fields:
   `url`, `type`, `borrow`, `conv` (1-9), `wow` (1-9). Strongly recommended:
   `name`, `styles`, `industry`, `source` (out-of-geo | gallery | team), `why`,
   `by` (your agent name).

5. **Validate + append.**
   ```bash
   python3 references/append_reference.py entries.json
   ```
   If it fails validation, fix the entries and re-run — the error messages name
   exactly what's wrong. `--dry-run` first if you want a no-risk pass.

6. **Commit and push.**
   ```bash
   git -C <repo> add references/ && git -C <repo> commit -m "refs: add N <vertical> entries" && git -C <repo> push
   ```
   Now every agent on every machine sees the additions.

## Vetting bar (do not relax it)

- Reject anything you can't name a specific borrow for. If you think "it just
  looks good", it fails the bar.
- Score honestly. A gallery find that wows at 9 but has no above-fold CTA is
  `wow: 9, conv: 3`. Do not pad `conv` because it looks expensive.
- 10 is forbidden on both axes (script caps at 9).
- Prefer 1-2 references per section type over 6 mediocre ones. Fewer, sharper.
- Screenshots (`shot` field) are a bonus — take them when the build will show
  the owner. Store under `references/shots/<name>.png`.

## Pitfalls

- **Mining the client's own market.** Same-city competitors are the field the
  client must beat; referencing them designs to the level of the competition.
  Go cross-market or cross-industry.
- **Award-site bias.** awwwards/CSSDA pages look unreal but often don't sell.
  Loading the library with gorgeous non-converters poisons the `conv` signal.
  The two-score system exists for this — use it.
- **Browsing when the library already covers it.** Re-mining a well-covered
  section wastes compute and adds dupes. Check first, browse second.
- **Forgetting to pull / push.** If you don't pull first, you duplicate entries
  other agents already added. If you don't push, your work is local-only and
  invisible to the next agent. Pull before mine, push after.
- **Skipping the script.** A hand-edit that drifts the format breaks every
  agent that parses the file. Always append through `append_reference.py`.
- **Copying copy/imagery.** References are for layout idea, spacing, treatment.
  Never log (or later build) another site's copy, images, or code wholesale.
