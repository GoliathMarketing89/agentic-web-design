---
name: agentic-web-design
description: Get good, converting design out of an AI coding agent. Use when building or redesigning a website, landing page, or web app with an agent — a mandatory taste-and-verify workflow that stops the agent from shipping generic AI output. Built by Goliath Marketing (goliathmarketing.io).
version: 2.0.0
author: Goliath Marketing
license: MIT
tags: [web-design, ui, landing-page, conversion, vibe-coding, cro, design-systems, agentic, astro]
platforms: [linux, macos, windows]
triggers:
  - build a website
  - design a landing page
  - make a page that converts
  - vibe code
  - web design
  - redesign my site
  - landing page that sells
  - agentic web design
---

# Agentic Web Design

The problem with AI-built sites is **taste**: agents default to generic, committee-pleasing output. This skill is a mandatory workflow that stops that. It runs the build through seven gates, and the gates that matter most — feeding the agent taste and critiquing its own work — are not optional.

**The rule that governs everything:** websites need to *convert*, not impress. Cinematic styling is garnish; conversion structure is the meal. Every creative decision gets checked against the conversion structure before it ships.

## How to use this skill

- **With a brief** (client, product, audience, goal): run the Goliath Build Loop below, in order. Do not skip a gate.
- **With a step name** (e.g. "taste" or "critic"): load that gate's instructions.
- **With a resource need**: load `resources.md` and read only the section the current gate points to. Do not read the whole shelf up front.

The toolbox lives in [resources.md](resources.md). The loop below is the operating procedure; the resources are what each step reaches for.

---

## The Goliath Build Loop

Run these gates in order. A gate is a hard stop: you do not move to the next step until the current one passes. If you are tempted to skip Gate 1 or Gate 4, you are about to produce the generic output this skill exists to prevent.

### Gate 0 — PRD (write it, get it approved)

Before any code, write a Product Requirements Document: what you are building, for whom, the one conversion action, and the message. Hand it to the user for approval. An agent with an approved PRD builds differently than an agent with a one-line prompt.

### Gate 1 — Taste (mandatory, before any code)

The single highest-leverage step, and the one agents skip. **Do not write code until this gate passes.**

1. Pick **one** design system from the taste layer (`resources.md` §2). Prefer `awesome-design-md` (50+ brand design languages as `DESIGN.md` files) or a real product style from Refero Styles.
2. Install it / load it into the agent's context.
3. Write `my_brand_design.md` — adapt the chosen system to the client's colors, fonts, and voice. This file is the taste contract for the whole build.
4. Only then start building.

If you skip this, the output will be generic. That is the failure mode this skill exists to prevent.

### Gate 2 — Direction (set a non-default direction)

Apply the creativity techniques (`resources.md` §1) so the build does not look like every other AI site. Pick one and state the direction in a single line before building:

- **Seed string** — generate a long random alphanumeric string, derive color/layout/typography from it. No two runs look the same.
- **Ambitious prompt** — name a real inspiration (a video game, an interior trend, an art installation) and how it should shape the output. "Radically asymmetric layout, dissonant colors, uncomfortable negative space. Break the rules but still make it look good."
- **Named reference** — point at a specific high-end site and say what to borrow.

### Gate 3 — Build (map to the conversion structure)

Build with the component stack (`resources.md` §3), mapped to the 9-block landing structure (`resources.md` §4). Know which block each section serves before you write it.

**Astro path (preferred):** use **Stardrive** (`astro-stardrive.com`, local copy at `/home/michael/stardrive`) as the boilerplate — it bakes in technical SEO, security, accessibility, and AI-agent-readiness (`AGENTS.md`, `.ai/` guides, `llms.txt`). Map the 9 blocks to Astro components, wire the design system into Astro's global CSS, and use Astro islands for interactive pieces. Keep the build static-first; add interactivity only where a block needs it.

**React/Next path:** shadcn/ui plus the component stack, same 9-block mapping.

### Gate 4 — Critic loop (mandatory)

The coding agent cannot critique its own work. Spawn a **fresh design-critic subagent** in a new context, given only a screenshot of the build. Ask it to score the design 1-10 against taste and the conversion structure. Loop until it independently scores **9/10 or higher**. Do not ship before it passes.

- Use a big, expensive model as the critic (executive judgment).
- Use a cheap, fast model as the implementer.

### Gate 5 — Conversion check (mandatory)

Run the 25-point conversion audit (`resources.md` §4). **Do not ship a page that fails items 1-5.** For a home-service client, also run the Home Service Playbook. For ecommerce, the Product Page CRO.

### Gate 6 — AI-tell audit (mandatory)

Strip every AI tell before shipping:

- Overdone effects and excessive decoration.
- Blue/purple gradients (the industry default) — use warm palettes, one accent color for CTAs, high contrast.
- Code-based gradients and shapes where a real image would do.
- Generic structure and padding.
- **Hand-rewrite the copy** — AI copy is a tell and lacks human voice. Run it through the `copywriting-master` skill if you need it to convert.

### Gate 7 — Ship

Ship. The build is done when it passes Gates 4, 5, and 6, not when the code compiles.

---

## Quick-start decision guide

| Job | Reach for |
|---|---|
| Give the agent taste (Gate 1) | `resources.md` §2 — awesome-design-md, Refero Styles, DESIGNmd, Jiro |
| Set a non-default direction (Gate 2) | `resources.md` §1 — seed strings, ambitious prompts |
| Build clean UI fast (Gate 3) | `resources.md` §3 — shadcn/ui, Aceternity, Magic UI, Motion Primitives |
| Add 3D / scroll-driven wow | `resources.md` §3 — ThreeUI, Scrolltide, Spline, Canvas UI |
| Add motion / icons / illustration | `resources.md` §3 — LottieFiles, Anime.js, 3D Icons, Kitbitz |
| Structure a landing page (Gate 3) | `resources.md` §4 — 9-block template + Hormozi prompt |
| Verify it converts (Gate 5) | `resources.md` §4 — 25-point audit, Home Service Playbook, Product Page CRO |
| Make it rank locally | `resources.md` §5 — Service Page SEO, Money Pages, Stardrive |
| Brand assets | `resources.md` §6 — ChatGPT Logo, Photo-to-Poster, PromptCard, Interior AI, Openverse |
| Ship it (Gate 7) | `resources.md` §7 — MVP Build Workflow, Vercel, Stardrive |

## Related skills in this repo

- **`copywriting-master`** — write the copy that sells before you build the page that holds it.
- **`seo-ranking`** — after the site is built, make it rank.
- **`local-link-building`** — build authority with genuine local links.

## Scope and limits

This skill produces the workflow and the toolbox for building converting sites with an agent. It does not guarantee a specific visual outcome — taste is enforced by the gates, not by the resources. The resources in `resources.md` are third-party tools; verify licenses and terms before shipping a client build. For regulated categories, have the copy and claims reviewed before publishing.
