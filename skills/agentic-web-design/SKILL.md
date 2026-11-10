---
name: agentic-web-design
description: Build or redesign websites through agreed UX and copy, visual section reference boards, a full-page storyboard, and iterative implementation and review.
license: MIT
metadata:
  version: 2.2.0
  author: Goliath Marketing
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

The problem with AI-built sites is **taste**: agents default to generic, committee-pleasing output. This skill is a mandatory workflow that stops that. It runs the build through a visible, collaborative process: agree the UX and copy, compare section references, agree a full-page storyboard, then implement and review.

**The rule that governs everything:** websites need to *convert*, not impress. Cinematic styling is garnish; conversion structure is the meal. Every creative decision gets checked against the conversion structure before it ships.

## How to use this skill

- **With a brief** (client, product, audience, goal): run the Goliath Build Loop below, in order. Do not skip a gate.
- **With a step name** (e.g. "taste" or "critic"): load that gate's instructions.
- **With a resource need**: load `resources.md` and read only the section the current gate points to. Do not read the whole shelf up front.

The toolbox lives in [resources.md](resources.md). The loop below is the operating procedure; the resources are what each step reaches for.

---

## The Goliath Build Loop

Run these gates in order. A gate is a hard stop: you do not move to the next step until the current one passes. The two gates agents skip — writing the copy first and pulling real design references per section — are the ones that separate a bespoke site from an AI template.

### Gate 0 — Establish the brief and proposed UX

Inspect the project folder, research, existing drafts, supplied material and working site before asking questions. Record audience, visitor task, primary action, required pages, brand, stack, content and asset constraints. Preserve decisions already made.

Propose the page and navigation structure for this visitor. Each section needs a job; select its place in the sequence from that job rather than applying a universal page formula. Resolve material gaps in the brief, then prepare the complete content outline in Gate 1.

### Gate 1 — Agree the full UX and copy

Present the complete page in reading order, with stable section IDs. For every section show:

- The visitor question, section purpose and reason for its position.
- Proposed headline, body copy, proof/content slots and image role.
- CTA label, destination and what happens after activation.

Draft usable copy before detailed layout, preserving good existing material. Use `copywriting-master` when available for persuasion and voice. Identify missing evidence rather than inventing reviews, credentials or results.

**Done when:** the designer has seen and agreed the complete UX/copy outline. Combine this into one useful review, not separate approvals for every sentence. Reuse explicit existing approvals; a broad mood or approved hero does not settle the rest of the page.

### Gate 2 — Agree visual references section by section

Read [section-review.md](section-review.md) for the required board and storyboard format.

**Use the library as visible choices.** Start with `references/design-reference-library.md` and its linked screenshots, gallery and rebuild notes. For each substantial section, prepare two or three meaningfully different, relevant examples using the proposed content. Select by visitor job, content shape and responsive behavior. Use `web-design-reference-miner` when available to fill genuine gaps; if the shared bank is unavailable, inspect suitable sources and record them in the project.

Show actual section screenshots, a short adaptation explanation and a recommendation. Include desktop and mobile evidence where available. Source links support the visuals; a list of URLs, style labels or private agent notes is not a visual review. Explain what structural idea a bento, editorial split, comparison or other pattern contributes to this content.

Let the designer choose and refine in a short round: for example, “services A, process B, make the case study more editorial.” Bring back only unresolved choices. Give sections below the hero the same deliberate selection treatment as the hero.

Assemble the selected directions into a full-page storyboard with the real copy, image roles and rough proportions. Check repetition, visual rhythm, light/dark balance, density, transitions and mobile order before implementation.

**Done when:** all required section jobs are covered and the designer has seen and agreed the visual boards and combined storyboard. Record selected example IDs, adaptations and approval scope in `design.md`. Explicit delegated direction can replace a human choice; still produce the boards/storyboard and document the recommendation used. Silence, a reference name or a hero-only approval is not approval of unseen sections.

### Gate 3 — Implement the agreed storyboard in small groups

Build selected section compositions around the agreed copy and brand. Translate the reference's hierarchy, proportions and asset role; changing colors on a stock card grid does not establish adaptation.

Start with a representative slice, then extend in small section groups, usually two or three. Show actual rendered desktop/mobile screenshots as groups are completed and compare them with their selected references. Keep these progress reviews lightweight. Routine spacing and execution fixes stay within existing authorization; a material layout, asset or content departure returns to a visible design choice before extending it across the site.

**Resolve asset direction before production.** Follow [asset-direction.md](asset-direction.md) for substantial site visuals: define the visitor meaning, brainstorm distinct concepts with the designer, choose a suitable route and scope paid production, then review a still with the real copy on desktop and mobile before expanding the asset set. Reuse existing approvals and caps. An unresolved concept needs feedback unless asset direction was explicitly delegated. Paid video is a separate motion and spending decision; neither a site-build request nor an approved still supplies an unlimited media budget.

**Pick the framework for the project, not for the skill.** The workflow is the same in any stack; only the components change.

- **Astro** — use **Stardrive** (`astro-stardrive.com`, local copy at `/home/michael/stardrive`) as the boilerplate: it bakes in technical SEO, security, accessibility, and AI-agent-readiness. Map the sections to Astro components, wire the design system into Astro's global CSS, use Astro islands for interactive pieces. Keep it static-first.
- **Webflow** — build the sections as Webflow sections. Use the design system for the style guide before you lay out sections. Keep interactions transform/opacity-only for performance.
- **React / Next** — shadcn/ui plus the component stack, same section mapping.

### Gate 4 — Animations (make it impressive, last)

Only after the design is built do you add motion. Animation is the polish layer, not the structure. Add it where it earns its place: a hero entrance, a scroll reveal, a hover state. Keep it transform/opacity-only for performance. Do not animate everything.

### Gate 5 — Critic loop (mandatory)

Use a fresh independent design critic when delegation is available and authorized. Provide the agreed UX/copy outline, selected section screenshots, storyboard, and rendered desktop/mobile page captures. If independent review is unavailable, label the separate self-review accordingly.

Judge each section against its chosen reference and the visitor task, then assess the page as a whole. Check distinctive composition, content-specific hierarchy, asset meaning, and variety that still feels like one site. A strong hero, clean typography or consistent colors cannot compensate for generic sections below it.

Record concrete findings, make a small batch of changes, and review fresh evidence. Retain the **9/10** target as a review bar, not a number to negotiate: unresolved material findings stay visible even when a score is high. After two passes without improvement, revisit the design choice with the designer instead of repeating cosmetic changes or encouraging a higher score. Distinguish draft visual quality from production readiness; a critic score does not establish Marketplace acceptance, functional correctness or conversion results.

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
| Map the UX outline (Gate 0) | visitor questions, navigation and section jobs; agree the full UX/copy at Gate 1 |
| Write the copy first (Gate 1) | the `copywriting-master` skill |
| Find per-section design references (Gate 2) | visual section boards and the full-page storyboard in `section-review.md` |
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

