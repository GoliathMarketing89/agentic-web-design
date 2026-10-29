# Agentic Web Design

Skills for building websites that look good **and** convert — and then rank.

Four skills, one workflow. Built by [Goliath Marketing](https://goliathmarketing.io)
from real client work and curated from the best of the web-design, SEO, and
copywriting community.

## The skills

| Skill | What it does | Use when |
|---|---|---|
| **`agentic-web-design`** | Get good, converting design out of an AI coding agent. The taste problem, the build stack, the conversion checks. | Building or redesigning any site, landing page, or web app with an agent |
| **`seo-ranking`** | Make a site rank on Google's first pages. Keyword research, on-page, technical, local SEO, Google Business Profile. | A site needs organic traffic |
| **`local-link-building`** | Build genuine local links. The earned-over-placed playbook: foundation, reclamation, sponsorship, press, outreach, 90-day plan. | A site needs authority and rankings |
| **`copywriting-master`** | Write copy that converts. An agentic loop (gather, position, desire, structure, write, humanize, verify) grounded in Schwartz, Whitman, and Vosler. | Any page, ad, or email that must sell |
| **`web-design-reference-miner`** | Find and vet design references for a build brief, then append them to the shared reference library. Mines out-of-geography competitors and design galleries. | The reference library is thin for a section type, or a maintenance pass to grow the library |

They chain together: **write** the copy that sells → **design** the site that
deserves to rank → **rank** it with on-page and technical SEO → **build
authority** with real local links.

## The shared reference library

`references/design-reference-library.md` is a vetted, per-section bank of real
sites. `agentic-web-design` pulls candidate references from it before it ever
touches a browser, and `web-design-reference-miner` grows it. Any agent — Hermes,
Claude Code / Codex / OpenCode / Goose, or a human — can contribute.

- **Contract:** `references/reference-spec.md` — the entry format, taxonomy, and
  vetting bar. Read this before adding.
- **Append script:** `references/append_reference.py` — the only supported way
  to add entries. Validates, dedupes by URL, re-sorts by section, caps scores
  at 9, rejects vague "nice clean layout" borrows.

```bash
# add one or more entries (see reference-spec.md for the schema)
python3 references/append_reference.py entries.json
```

## Install

### Via skills.sh

```bash
npx skills add goliathmarketing89/agentic-web-design
```

### Individual skills

```bash
npx skills add goliathmarketing89/agentic-web-design/agentic-web-design
npx skills add goliathmarketing89/agentic-web-design/seo-ranking
npx skills add goliathmarketing89/agentic-web-design/local-link-building
npx skills add goliathmarketing89/agentic-web-design/copywriting-master
```

### Manual

Copy the skill folder you want into your agent's skills directory. Each skill
is self-contained — a single `SKILL.md` with everything the agent needs.

## The philosophy

**Websites need to convert, not impress.** Cinematic styling is garnish;
conversion structure is the meal. Every skill in this repo is built around that
rule — design for conversion, rank for traffic, build authority with links that
would make sense even if search didn't exist.

## License

MIT. See [LICENSE](LICENSE).

## About

Built by [Goliath Marketing](https://goliathmarketing.io) — web design, SEO, and
local link building for small local service businesses. These skills are the
workflow we use on every client build, open-sourced.

## Contributing

Open to contributions. The bar: real, tested, non-obvious value. If a tactic
doesn't survive the "would I have anything to explain away?" test, it doesn't
belong here.
