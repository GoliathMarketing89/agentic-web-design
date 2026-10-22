---
name: agentic-web-design
description: Get good, converting design out of an AI coding agent. Use when building or redesigning a website, landing page, or web app with an agent — the taste problem, the build stack, and the conversion checks that separate a page that converts from one that just looks pretty.
version: 1.0.0
author: Goliath Marketing
license: MIT
tags: [web-design, ui, landing-page, conversion, vibe-coding, cro, design-systems, agentic]
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

The core problem with AI-built sites is **taste**: agents default to generic,
committee-pleasing output. This skill is the workflow for getting on-brand,
converting UI out of a coding agent — the method, the taste layer, the build
stack, and the conversion checks.

**The rule that governs everything:** websites need to *convert*, not impress.
Cinematic styling is garnish; conversion structure is the meal. Always verify
creative output against the conversion checks in section 4.

## When to use this skill

- Building or redesigning any website, landing page, or web app with an AI agent
- A vibe-coded build that needs to look good AND convert
- A client site (home services, local business, SaaS) that must turn visitors into leads
- Any time an agent's default output looks "AI-generated" and you need real taste

For a formal DESIGN.md token spec file, use the `design-md` skill. For a
specific brand's visual language (Stripe, Linear, Vercel), pair with
`popular-web-designs`. This skill is the *workflow* that ties taste, build, and
conversion together.

## The method — how to get good design out of an agent

### 1. Write the PRD first

Before any code, generate a Product Requirements Document: what you're building,
for whom, the one conversion action, the message. Hand it to the agent with
clearly communicated goals. An agent with a PRD builds differently than an
agent with a one-line prompt.

### 2. Feed the agent taste BEFORE it writes code

The single highest-leverage step. Load reference material into the agent's
context *before* it starts building, so it knows what good looks like:

- **awesome-design-md** — `github.com/VoltAgent/awesome-design-md` — design
  languages of 50+ major brands (Apple, Spotify, IBM) compressed into one
  `DESIGN.md` per brand: palettes, fonts, reference components. Share the repo
  with the agent, let it install, tell it to use the spec as reference. Tip:
  ask it to adapt a brand's system to your colors and save as
  `my_brand_design.md` so the taste is yours.
- **make-interfaces-feel-better** — Claude Code skill by Jakub Krehel, 30k+
  installs. UI/animation/performance polish tips. Install:
  `npx skills add jakubkrehel/make-interfaces-feel-better`
- **Design prompt libraries** — Jiro (jiro.build, 1200+ AI-ready prompts),
  Minimal Gallery (minimal.gallery), Kage (kage.design), Refero Styles
  (styles.refero.design, 2000+ real product styles), Component Gallery
  (component.gallery, 2600+ examples), DESIGNmd (designmd.ai).

**Lightweight variant:** use Playwright to grab visual inspiration from
carefully-chosen reference sites, throw in a brand voice skill + a front-end
design skill. Trade: taste comes from whatever pages you point Playwright at,
so choose reference sites carefully.

### 3. Push the agent past its bland defaults (8 techniques)

1. **Seed strings** — have the agent generate a long random alphanumeric string
   via shell script, then derive the creative direction (color, layout,
   typography) from it. No two runs produce the same design.
2. **Be more ambitious with prompts** — bring your own taste in. Describe an
   inspiration (a video game, an interior trend, an art installation) and how it
   should influence output. "Radically asymmetric layout, dissonant colors,
   uncomfortable negative space. Break all the rules but still make it look good."
3. **Positive feedback loops with subagents** — the coding agent can't critique
   its own work. Invoke a separate "design critic" subagent in a fresh context,
   given only a screenshot. Loop until it independently scores 9/10+. Use a big
   expensive model as critic (executive decisions), a cheap fast model as
   implementer.
4. **Use image generation to enrich designs** — coding agents default to
   code-based gradients/shapes (all AI tells). Push them to use real images.
   Connect via built-in tools, Codex CLI, or a dedicated API key in a gitignored
   `.env.agents` file.
5. **Use video generation for advanced motion** — animated graphics (loop on
   solid bg, chroma-key out, layer in) and fluid transitions between states.
   Use an aggregator like fal.ai for one API key.
6. **Cut elements that don't add value** — AI adds, rarely subtracts. Restraint
   reads as premium. Most polishing is removal.
7. **Remove AI tells** — strip overdone effects, excessive decoration, generic
   structure.
8. **Rewrite copy by hand** — AI copy is a tell and lacks human voice.

## The taste layer — where to point the agent before it writes code

| Tool | URL | What it is |
|---|---|---|
| Jiro | jiro.build | 1200+ AI-ready design prompts |
| Minimal Gallery | minimal.gallery | Curated high-end sites to feed your agent |
| Kage | kage.design | Real UI inspiration mapped straight to prompts |
| Refero Styles | styles.refero.design | 2,000+ real product styles with typography |
| Component Gallery | component.gallery | 2,600+ examples of how top design systems solve the same element |
| AppShot Gallery | appshot.gallery | Real app screenshots for mobile |
| DESIGNmd | designmd.ai | Design systems as markdown your agent can read |
| VibePrompt | vibeprompts.dev | Ready-made prompts for dashboards and landing pages |
| 21st.dev | 21st.dev | Component registry that plugs into agents via MCP |
| Kinetics | kinetics.colorion.co | 150+ motion effects with React code and prompts |

**Design inspiration galleries** (the "pieces of a page" shelf): inspora.design
(visual), posts.design (social), loadmo.re (mobile), mobbin.com (UI screens,
signup-gated), recent.design, 60fps.design (UI animation), supahero.io (hero
sections), navbar.gallery, cta.gallery, logobook.com (logos), pageflows.com
(dashboards), component.gallery (design systems).

## The build layer — the actual building blocks

### Core UI stacks (fast, clean)

| Tool | URL | What it is |
|---|---|---|
| shadcn/ui | ui.shadcn.com | The gold standard for clean, reusable UI |
| Aceternity UI | ui.aceternity.com | 200+ animated React/Tailwind components |
| Magic UI | magicui.design | Beautifully designed components for modern web apps |
| Motion Primitives | motion-primitives.com | Ready-to-use animation and interaction components |
| Uiverse | uiverse.io | Community-built UI elements |
| UIAble | uiable.com | Ready-to-use UI components |
| mapcn | mapcn.dev | Map components, markers, routes, popups |
| MicroKit UI | microkit.co | Micro-interactions that make interfaces feel polished |
| Liquid Glass | glass.samasante.com | Glass refraction components and effects |
| CSS Text Effects | text-effects.colorion.co | Creative CSS text animations |
| Circle Loaders | circleloaders.dominikakissi.com | Loading animations and loaders |
| Gradient Buttons | gradientbuttons.colorion.co | Gradient button styles |

### 3D / WebGL / scroll-driven (the visual upgrade layer)

- **ThreeUI** — threeui.com / github.com/MengTo/threeui — Meng To's open-sourced
  three.js component library. 160+ free components and landing pages. Every
  component copyable as a prompt or source — hand the prompt to an agent, tell it
  to change theme/lighting/motion/layout. MIT. **Caveat:** 100–200 KB per
  component + WebGL runtime; perf-test, not every site needs 3D.
- **Canvas UI** — canvasui.dev — David Haz's html-in-canvas + WebGL effects
  library. 33 components (Particle Reveal, Liquid, Glass, Shatter, VHS, Clouds,
  Ripple...), each in React/Solid/Preact/Vue/Svelte/vanilla TS. Install via
  shadcn CLI. MCP-ready. MIT + Commons Clause. **Caveat:** live-HTML-on-canvas
  needs a Chrome flag; WebGL effects degrade gracefully elsewhere.
- **Scrolltide** — scrolltide.co — 600+ design prompts with full source code for
  3D and scroll-driven sites. 124 templates, 66 components, 55 shaders. $299
  one-time lifetime; some free. Engineered for Claude/Cursor/v0.
- **Spline** — spline.design — 3D design for the web, browser-based, exports to
  Web/Webflow/React/Next.js.
- **Three.js Journey** — threejs-journey.com — learn 3D on the web, step by step.

### Animation / icons / illustration

- **LottieFiles** — lottiefiles.com — ready-made lightweight animations; 800k+ free & premium.
- **Anime.js** — animejs.com — lightweight JavaScript animation library.
- **3D Icons** — 3dicons.co — 1500+ hand-made 3D icons, CC0 (free commercial use).
- **Kitbitz** — kitbitz.art — 2,000+ hand-drawn illustrations.

## The conversion layer — the meal, not the garnish

Creative is garnish. These are the blocks that make a page convert. **Verify
every build against these.**

### Landing Page Structure Template (9 blocks)

1. **Hero** — H1 value prop; 2-sentence product description; product visual
   (video demo or annotated screenshot); one big CTA; quick social proof.
2. **Problem agitation** — Point A the customer hates; specific negative
   consequences of not solving it.
3. **Transformation** — Point B the customer desires; specific positive benefits.
4. **Social proof** — 5-7 testimonials with photo + role; bonus: opinion-leader endorsements.
5. **Features** — 3-4 "how it works" steps or power features; zero technical language.
6. **About us** — why you built it; what else you've built; media mentions.
7. **Pricing** — 2-3 plans (downsell, main, upsell); transparent refund policy.
8. **FAQ** — 5-7 tough objections answered directly.
9. **Final CTA** — repeat value prop; big CTA button.

**Hormozi-style generation prompt rules:** headline pattern "Get [TARGET] To
[OUTCOME] Without [FRUSTRATION]"; **NO blue/purple gradients** (overused in AI
industry) — warm palettes, single accent color for CTAs, high contrast; Core Web
Vitals targets (LCP < 2.5s, CLS < 0.1); transform/opacity-only animations;
mobile-first; no external deps except icons.

### 25-point conversion audit

Scores any landing/sales page against 25 points. On new builds, don't ship a
page that fails items 1-5. Highlights: headline 4-U formula; above-fold value
prop; first-person CTA; 5-field form max; ad-to-page message match; social proof
near CTAs; cognitive bias stack; PAS copy; genuine urgency only; price anchoring;
F-pattern visual hierarchy; mobile thumb zone; grade-6 reading level; white space
= focus; benefit-first language; micro-commitment ladder.

### Home Service Website Conversion Playbook

For home-service clients (the vertical that pays the bills). Five points:

1. **Hero answers three questions in under two seconds** — what you do, where,
   how to reach you. Big headline naming the service, city under it, visible
   phone number, real photo of actual work (never stock).
2. **Trust signals where they can't be missed** — Google rating + review count
   up top; licensed/insured, locally owned, years in business as simple icons.
3. **Booking stupid easy, more than one way** — tap-to-call button that sticks
   while scrolling, bare-minimum form, online scheduling.
4. **Mobile-first** — traffic is on a phone standing in a kitchen. Fast load,
   big tap targets, CTA within thumb reach.
5. **Ad traffic gets its own landing pages, separate from SEO pages** — SEO
   pages are long (need content to rank); ad pages are stripped to one service,
   trust signals, one action.

**Speed to lead:** the best-converting homepage still loses the job if nobody
answers the phone for an hour. Instant response converts. Budget for a human (or
fast call-answering system) on the phone during business hours.

### High-Converting Product Page (6 elements)

For ecommerce product pages: urgency-inducing toolbar (free shipping threshold +
promo code); improved imagery (product in real life, not sterile studio); social
proof integration (star rating + "Loved By Hundreds"); benefit-driven bullet
points (quantified); flexible purchase options (one-time + subscription);
streamlined checkout (multiple trusted payments + prominent Add to Cart).

## The verify step — kill the AI tells before you ship

1. **Design critic loop** — invoke a separate "design critic" subagent in a
   fresh context, given only a screenshot. Loop until it independently scores
   9/10+. Big expensive model as critic, cheap fast model as implementer.
2. **Conversion check** — run the 25-point audit. Don't ship a page that fails
   items 1-5.
3. **AI-tell audit** — strip overdone effects, excessive decoration, generic
   structure, blue/purple gradients, code-based gradients/shapes.
4. **Hand-rewrite the copy** — AI copy is a tell and lacks human voice.

## Quick-start decision guide

| Job | Reach for |
|---|---|
| Give the agent taste | awesome-design-md, Minimal Gallery, Refero Styles, DESIGNmd, Jiro |
| Build clean UI fast | shadcn/ui, Aceternity, Magic UI, Motion Primitives |
| Add 3D / scroll-driven wow | ThreeUI, Scrolltide, Spline, Canvas UI |
| Add motion / icons / illustration | LottieFiles, Anime.js, 3D Icons, Kitbitz |
| Structure a landing page | 9-block template + Hormozi prompt |
| Verify it converts | 25-point audit, Home Service Playbook, Product Page CRO |
| Make it rank locally | see the `seo-ranking` skill |
| Build authority with links | see the `local-link-building` skill |
| Brand assets | ChatGPT Logo, Photo-to-Poster, PromptCard, Interior AI, Openverse |

## Related skills in this repo

- **`seo-ranking`** — after the site is built, make it rank: keyword research,
  on-page optimization, technical SEO, local SEO, Google Business Profile.
- **`local-link-building`** — build authority with genuine local links: the
  playbook for earned-over-placed link building for a local service business.

## Sources

Curated from Michael's X bookmarks and the Goliath Marketing web-design
workflow. Primary sources: Vibe-Coding Design That Converts (The Boring
Marketer), AI Design Creativity (Anshu Chimala's 8 Techniques), Landing Page
Structure Template (Dan Kulkov), Home Service Website Conversion Playbook (Noah
Igler), High-Converting Product Page (Oliver Kenyon), and the design resource
shelves (Aman Singh, Abraham John, Vullnet Ademaj, Tanzil Chowdhury).
