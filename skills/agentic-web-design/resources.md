# Agentic Web Design — Resource Shelf

The toolbox for the Goliath Build Loop. Read only the section the current gate points to. Each section is a shelf; pick what the job needs.

---

## §1 The method — how to get good design out of an agent

The core problem is taste: agents default to generic output. These methods fix that.

### Vibe-Coding Design That Converts
1. Generate a PRD for what you're building.
2. Hand it to the agent with clearly communicated goals.
3. Grab real design tokens (e.g. Tailwind assets from Figma via the Anima plugin) — not guesswork.
4. Give the agent great designs to reference — load them into context as reference material.
5. Let the agent understand what good looks like *before* writing code.
6. Start building the prototype.

### AI Design Creativity — 8 techniques to push past bland defaults
1. **Seed strings** — generate a long random alphanumeric string via shell script, derive the creative direction (color, layout, typography) from it. No two runs produce the same design.
2. **Be more ambitious with prompts** — bring your own taste in. Describe an inspiration (a video game, an interior trend, an art installation) and how it should influence output. "Radically asymmetric layout, dissonant colors, uncomfortable negative space. Break all the rules but still make it look good."
3. **Positive feedback loops with subagents** — the coding agent can't critique its own work. Invoke a separate "design critic" subagent in a fresh context, given only a screenshot. Loop until it independently scores 9/10+. Big expensive model as critic, cheap fast model as implementer.
4. **Use image generation to enrich designs** — coding agents default to code-based gradients/shapes (all AI tells). Push them to use real images. Connect via built-in tools, Codex CLI, or a dedicated API key in a gitignored `.env.agents` file.
5. **Use video generation for advanced motion** — animated graphics (loop on solid bg, chroma-key out, layer in) and fluid transitions between states. Use an aggregator like fal.ai for one API key.
6. **Cut elements that don't add value** — AI adds, rarely subtracts. Restraint reads as premium. Most polishing is removal.
7. **Remove AI tells** — strip overdone effects, excessive decoration, generic structure.
8. **Rewrite copy by hand** — AI copy is a tell and lacks human voice.

---

## §2 Taste layer — where to point the agent before it writes code (Gate 1)

| Tool | URL | What it is |
|---|---|---|
| awesome-design-md | github.com/VoltAgent/awesome-design-md | Design languages of 50+ major brands (Apple, Spotify, IBM) as one `DESIGN.md` per brand. Share the repo, let the agent install, adapt to your colors as `design.md`. |
| make-interfaces-feel-better | `npx skills add jakubkrehel/make-interfaces-feel-better` | UI/animation/performance polish tips. |
| Jiro | jiro.build | 1200+ AI-ready design prompts. |
| Minimal Gallery | minimal.gallery | Curated high-end sites to feed your agent. |
| Kage | kage.design | Real UI inspiration mapped straight to prompts. |
| Refero Styles | styles.refero.design | 2,000+ real product styles with typography. |
| Component Gallery | component.gallery | 2,600+ examples of how top design systems solve the same element. |
| AppShot Gallery | appshot.gallery | Real app screenshots for mobile. |
| DESIGNmd | designmd.ai | Design systems as markdown your agent can read. |
| VibePrompt | vibeprompts.dev | Ready-made prompts for dashboards and landing pages. |
| 21st.dev | 21st.dev | Component registry that plugs into agents via MCP. |
| Kinetics | kinetics.colorion.co | 150+ motion effects with React code and prompts. |

**Design inspiration galleries** (the "pieces of a page" shelf): inspora.design (visual), posts.design (social), loadmo.re (mobile), mobbin.com (UI screens, signup-gated), recent.design, 60fps.design (UI animation), supahero.io (hero sections), navbar.gallery, cta.gallery, logobook.com (logos), pageflows.com (dashboards), component.gallery (design systems), awwwards.com, siteinspire.com, land-book.com, lapa.ninja, onepagelove.com, typewolf.com (typography), coolors.co (palettes), huemint.com (palette generation).

---

## §3 Build layer — the actual building blocks (Gate 3)

### Core UI stacks (fast, clean)
| Tool | URL | What it is |
|---|---|---|
| shadcn/ui | ui.shadcn.com | The gold standard for clean, reusable UI. |
| Aceternity UI | ui.aceternity.com | 200+ animated React/Tailwind components. |
| Magic UI | magicui.design | Beautifully designed components for modern web apps. |
| Motion Primitives | motion-primitives.com | Ready-to-use animation and interaction components. |
| Uiverse | uiverse.io | Community-built UI elements. |
| UIAble | uiable.com | Ready-to-use UI components. |
| mapcn | mapcn.dev | Map components, markers, routes, popups. |
| MicroKit UI | microkit.co | Micro-interactions that make interfaces feel polished. |
| Liquid Glass | glass.samasante.com | Glass refraction components and effects. |
| CSS Text Effects | text-effects.colorion.co | Creative CSS text animations. |
| Circle Loaders | circleloaders.dominikakissi.com | Loading animations and loaders. |
| Gradient Buttons | gradientbuttons.colorion.co | Gradient button styles. |

### 3D / WebGL / scroll-driven (the visual upgrade layer)
- **ThreeUI** — threeui.com / github.com/MengTo/threeui — Meng To's open-sourced three.js library. 160+ free components and landing pages, each copyable as a prompt. MIT. **Caveat:** 100-200 KB per component + WebGL runtime; perf-test, not every site needs 3D.
- **Canvas UI** — canvasui.dev — David Haz's html-in-canvas + WebGL effects. 33 components (Particle Reveal, Liquid, Glass, Shatter, VHS, Clouds, Ripple), each in React/Solid/Preact/Vue/Svelte/vanilla TS. Install via shadcn CLI. MCP-ready. **Caveat:** live-HTML-on-canvas needs a Chrome flag; WebGL degrades gracefully elsewhere.
- **Scrolltide** — scrolltide.co — 600+ design prompts with full source for 3D and scroll-driven sites. 124 templates, 66 components, 55 shaders. $299 one-time; some free.
- **Spline** — spline.design — 3D design for the web, browser-based, exports to Web/Webflow/React/Next.js.
- **Three.js Journey** — threejs-journey.com — learn 3D on the web.

### Animation / icons / illustration
- **LottieFiles** — lottiefiles.com — ready-made lightweight animations; 800k+ free & premium.
- **Anime.js** — animejs.com — lightweight JavaScript animation library.
- **3D Icons** — 3dicons.co — 1500+ hand-made 3D icons, CC0.
- **Kitbitz** — kitbitz.art — 2,000+ hand-drawn illustrations.

---

## §4 Conversion structure — the meal, not the garnish (Gates 3, 5)

Creative is garnish. These blocks make a page convert. **Verify every build against these.**

### Landing Page Structure Template (9 blocks)
1. **Hero** — H1 value prop; 2-sentence product description; product visual (video demo or annotated screenshot); one big CTA; quick social proof.
2. **Problem agitation** — Point A the customer hates; specific negative consequences of not solving it.
3. **Transformation** — Point B the customer desires; specific positive benefits.
4. **Social proof** — 5-7 testimonials with photo + role; bonus: opinion-leader endorsements.
5. **Features** — 3-4 "how it works" steps or power features; zero technical language.
6. **About us** — why you built it; what else you've built; media mentions.
7. **Pricing** — 2-3 plans (downsell, main, upsell); transparent refund policy.
8. **FAQ** — 5-7 tough objections answered directly.
9. **Final CTA** — repeat value prop; big CTA button.

**Hormozi-style generation prompt rules:** headline pattern "Get [TARGET] To [OUTCOME] Without [FRUSTRATION]"; **NO blue/purple gradients** — warm palettes, single accent color for CTAs, high contrast; Core Web Vitals targets (LCP < 2.5s, CLS < 0.1); transform/opacity-only animations; mobile-first; no external deps except icons.

### 25-point conversion audit
Scores any landing/sales page against 25 points. On new builds, don't ship a page that fails items 1-5. Highlights: headline 4-U formula; above-fold value prop; first-person CTA; 5-field form max; ad-to-page message match; social proof near CTAs; cognitive bias stack; PAS copy; genuine urgency only; price anchoring; F-pattern visual hierarchy; mobile thumb zone; grade-6 reading level; white space = focus; benefit-first language; micro-commitment ladder.

### Home Service Website Conversion Playbook
1. **Hero answers three questions in under two seconds** — what you do, where, how to reach you. Big headline naming the service, city under it, visible phone number, real photo of actual work (never stock).
2. **Trust signals where they can't be missed** — Google rating + review count up top; licensed/insured, locally owned, years in business as simple icons.
3. **Booking stupid easy, more than one way** — tap-to-call button that sticks while scrolling, bare-minimum form, online scheduling.
4. **Mobile-first** — traffic is on a phone standing in a kitchen. Fast load, big tap targets, CTA within thumb reach.
5. **Ad traffic gets its own landing pages, separate from SEO pages** — SEO pages are long; ad pages are stripped to one service, trust signals, one action.

**Speed to lead:** the best-converting homepage still loses the job if nobody answers the phone for an hour. Instant response converts.

### High-Converting Product Page (6 elements)
Urgency-inducing toolbar (free shipping threshold + promo code); improved imagery (product in real life, not sterile studio); social proof integration (star rating + "Loved By Hundreds"); benefit-driven bullet points (quantified); flexible purchase options (one-time + subscription); streamlined checkout (multiple trusted payments + prominent Add to Cart).

---

## §5 Local SEO for design (make the site rank)

- **Service Page SEO That Ranks** — one page per service; H1 is service + city said plainly ("Roof Replacement in Clifton NJ"); ~1,000 words then out-length whoever ranks above you; real job case studies on the page (town, cost, time, photos); embed a custom Google My Map; a section about the city itself.
- **Local SEO Money Pages** — one comparison-style money page ("Best AC repair in Austin (2026)") instead of 50 blog posts. Name the buyer problem, compare real options, explain cost/risk in plain English, give AI/search something clean to cite, turn confused visitors into ready leads.
- **Rank-and-Rent (keyword + city)** — stack: Cloudflare, GitHub, Codex/Claude, Vercel. Pick an available keyword-plus-city domain with search demand, map service-area pages and silo structure.
- **Stardrive** — astro-stardrive.com / github.com/peltmonger/stardrive — free MIT Astro boilerplate that bakes in technical SEO, security, accessibility, and AI-agent-readiness. Ships `AGENTS.md`, `.ai/` guides, `CLAUDE.md`, `.cursorrules`, `llms.txt`. Local copy at `/home/michael/stardrive`.

---

## §6 Image & logo generation (brand assets)

- **ChatGPT Logo Generation** — 4 steps: GPT-4 Vision analyzes a reference logo; ask for a DALL-E prompt; generate in DALL-E 3 with your business name; iterate conversationally.
- **Photo to Minimalist Poster Prompt** — reusable prompt turning each photo into a standalone high-end minimalist poster: original photo on top, geometric abstraction below, 3:4 vertical, two equal zones.
- **PromptCard** — promptcard.net — Chrome extension that reverse-engineers prompts from images.
- **Interior AI** — interiorai.com — transforms photos of interiors/exteriors/gardens into redesigned renders; useful for before/afters and real-estate clients.
- **Free Media Libraries** — openverse.org (800M+ openly licensed images/audio, license-clear) and sound-effects.bbcrewind.co.uk (30,000+ BBC sound effects).

---

## §7 Build & ship stack

- **MVP Build Workflow** — 9-step: plan with ChatGPT/Gemini → design with UX Pilot → build UI with Lovable (70-80% of frontend visually, Supabase for data) → refine with Cursor + Claude Code, CodeRabbit, Taskmaster → ship on Vercel.
- **Vibe Coding — Config Constants Pattern** — ask the agent to make every system *configurable* with a constants file. Cheap, high-leverage for vibe-coded builds.
- **Codex Slides** — open-design.ai/codex-slides — open-source AI slide studio inside Codex. Exports pptx/pdf.

---

## Agent-specific tools (Hermes can use these directly)

- **shadcn MCP** — the shadcn protocol lets an agent browse, read docs, and install components from a single prompt (used by Canvas UI and 21st.dev).
- **awesome-design-md** — share the repo link with the agent, let it install/config, tell it to use the design spec as reference.
- **make-interfaces-feel-better** — `npx skills add jakubkrehel/make-interfaces-feel-better`.
- **ThreeUI prompts** — every component copyable as a prompt; hand to agent, tell it to change theme/lighting/motion/layout.
- **Scrolltide prompts** — paste into Claude/Cursor/v0 for 3D/scroll-driven sections.
- **fal.ai** — one API key for image/video gen, agent picks the best current model.
