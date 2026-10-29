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

Run these gates in order. A gate is a hard stop: you do not move to the next step until the current one passes. The two gates agents skip — writing the copy first and pulling real design references per section — are the ones that separate a bespoke site from an AI template.

### Gate 0 — Goal & UX outline (decide before anything)

1. **Name the one goal of the site.** What are we trying to get the visitor to do? Most sites have one: buy, generate a lead, contact, book. It's the big CTA in the top-right corner. Write it down.
2. **Map the homepage and nav.** Section by section, top to bottom: what is the hero's goal, what is the next section's goal, and the next. Each section has a job. The standard arc: hero → problem → solution → proof → how it works → about → pricing → FAQ → final CTA → footer (or an email-capture block, depending on the goal).
3. **Discuss the look with the user — back and forth, not a one-shot.** Before building, ask what they want it to feel like: references they like, a mood, a direction. Push back and refine until you both agree on the direction. Do not pump out a build and hope. This conversation is where the taste gets set.
4. Write the outline as a list of sections, each with its goal. Get it approved before writing copy.

### Gate 1 — Copy first (write the words before the design)

Once the outline is decided, write the proposed copy for each section. It does not have to be final or amazing — but you must know what goes in each section before you design it. The design adapts to the copy, not the other way around.

- Write the headline, subhead, section intros, and CTA for each section from the outline.
- Run it through the `copywriting-master` skill if it needs to convert.
- The copy is the content the design will carry. Do not design empty boxes and fill them later.

### Gate 2 — Design references per section (the step that kills the AI look)

This is the gate that was missing. **Do not design from memory or from a generic template.** For EACH section in the outline, find 1-2 interesting design references for that *type* of section — not "DJ websites" or "plumbing sites," but interesting heroes, interesting testimonial sections, interesting pricing sections, interesting FAQ sections.

**Pull from the shared library first, browse only when it's thin.** The
reference library at `references/design-reference-library.md` (in this repo) is
a vetted, per-section bank of real sites with what-to-borrow notes and conv/wow
scores. Check it before you touch a gallery. For each section type in your
outline, grep the matching `## <type>` block and shortlist 1-2 entries that fit
the brief. Then **show the owner the shortlist — names/URLs and what you'd
borrow — and get them agreed before building.** This is the reference
conversation; never quietly pick references and build. If the library has
nothing that fits a section type, run the `web-design-reference-miner` skill to
find and vet some (that skill mines out-of-geography competitors and galleries,
then appends vetted entries back through `references/append_reference.py`).

Only after the library is checked do you reach for the inspiration galleries
(`resources.md` §2): awwwards, siteinspire, land-book, refero, minimal.gallery,
supahero (heroes), cta.gallery, pageflows, etc.

- **Hero** → find an interesting hero layout, not a DJ hero.
- **Testimonials** → find an interesting testimonial section.
- **Pricing** → find an interesting pricing section.
- And so on for every section.

Save the references (URLs + what to borrow from each) in `design.md`. The build adapts these references to the copy and the brand — it does not invent a layout from scratch.

### Gate 3 — Build to the references

Build each section by adapting its design reference to the copy and the brand. Do not invent a generic layout — take the structure, spacing, and visual idea from the reference and fill it with the copy from Gate 1 and the brand from `design.md`.

**Grab real assets — images and video — as part of the build.** A site with real imagery beats one built from code-based shapes and gradients. For each section that needs a visual, source it: generate it (image/video gen), pull from a stock library, or use a client-provided asset. A hero background video, real product photos, or a genuine portrait transforms a design. Do not leave a section as empty boxes or code-only decoration when a real asset would carry it.

**Pick the framework for the project, not for the skill.** The workflow is the same in any stack; only the components change.

- **Astro** — use **Stardrive** (`astro-stardrive.com`, local copy at `/home/michael/stardrive`) as the boilerplate: it bakes in technical SEO, security, accessibility, and AI-agent-readiness. Map the sections to Astro components, wire the design system into Astro's global CSS, use Astro islands for interactive pieces. Keep it static-first.
- **Webflow** — build the sections as Webflow sections. Use the design system for the style guide before you lay out sections. Keep interactions transform/opacity-only for performance.
- **React / Next** — shadcn/ui plus the component stack, same section mapping.

### Gate 4 — Animations (make it impressive, last)

Only after the design is built do you add motion. Animation is the polish layer, not the structure. Add it where it earns its place: a hero entrance, a scroll reveal, a hover state. Keep it transform/opacity-only for performance. Do not animate everything.

### Gate 5 — Critic loop (mandatory)

The coding agent cannot critique its own work. Spawn a **fresh design-critic subagent** in a new context, given only a screenshot of the build AND the design references it was built from. Ask it to score the design 1-10 against the references and the conversion structure. Loop until it independently scores **9/10 or higher**. Do not ship before it passes.

- Use a big, expensive model as the critic (executive judgment).
- Use a cheap, fast model as the implementer.

### Gate 6 — Conversion check (mandatory)

Run the 25-point conversion audit (`resources.md` §4). **Do not ship a page that fails items 1-5.** For a home-service client, also run the Home Service Playbook. For ecommerce, the Product Page CRO.

### Gate 7 — AI-tell audit, human review & ship

Strip every AI tell before shipping:

- Overdone effects and excessive decoration.
- Blue/purple gradients (the industry default) — use warm palettes, one accent color for CTAs, high contrast.
- Code-based gradients and shapes where a real image would do.
- Generic structure and padding — if a section looks like a template, it is not adapted enough to its reference.
- **Hand-rewrite the copy** — AI copy is a tell and lacks human voice.

**Human review before ship.** Put the build in front of the user and get their read before calling it done. The critic loop scores it against references; the human decides if it actually feels right. Iterate on their feedback, then ship. The build is done when it passes Gates 5, 6, and 7, not when the code compiles.

---

## Quick-start decision guide

| Job | Reach for |
|---|---|
| Map the UX outline (Gate 0) | the standard arc: hero → problem → solution → proof → how it works → about → pricing → FAQ → CTA |
| Write the copy first (Gate 1) | the `copywriting-master` skill |
| Find per-section design references (Gate 2) | `resources.md` §2 — awwwards, siteinspire, land-book, refero, minimal.gallery, supahero, cta.gallery, pageflows |
| Build to the references (Gate 3) | `resources.md` §3 — shadcn/ui, Aceternity, Magic UI, Motion Primitives |
| Add 3D / scroll-driven wow | `resources.md` §3 — ThreeUI, Scrolltide, Spline, Canvas UI |
| Add motion / icons / illustration (Gate 4) | `resources.md` §3 — LottieFiles, Anime.js, 3D Icons, Kitbitz |
| Verify it converts (Gate 6) | `resources.md` §4 — 25-point audit, Home Service Playbook, Product Page CRO |
| Make it rank locally | `resources.md` §5 — Service Page SEO, Money Pages, Stardrive |
| Brand assets | `resources.md` §6 — ChatGPT Logo, Photo-to-Poster, PromptCard, Interior AI, Openverse |
| Ship it (Gate 7) | `resources.md` §7 — MVP Build Workflow, Vercel, Stardrive |

## Related skills in this repo

- **`copywriting-master`** — write the copy that sells before you build the page that holds it.
- **`seo-ranking`** — after the site is built, make it rank.
- **`local-link-building`** — build authority with genuine local links.

## Scope and limits

This skill produces the workflow and the toolbox for building converting sites with an agent. It does not guarantee a specific visual outcome — taste is enforced by the gates, not by the resources. The resources in `resources.md` are third-party tools; verify licenses and terms before shipping a client build. For regulated categories, have the copy and claims reviewed before publishing.
