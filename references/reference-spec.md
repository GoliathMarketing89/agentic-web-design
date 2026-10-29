# Design Reference Library — Contribution Spec

The shared reference library for Goliath's web-design work. Any agent — Hermes,
Claude Code / Codex / OpenCode / Goose, Claude/ChatGPT in a browser — can read it
and expand it. The spec guarantees every entry lands the same way no matter who
writes it.

## Where things live

- **Library file:** `references/design-reference-library.md` (in this repo)
- **This spec:** `references/reference-spec.md`
- **Append script:** `references/append_reference.py` (run this to add entries)
- **Screenshots:** `references/shots/<name>.png` (optional; reference by path)

## The one rule that governs everything

Websites convert, they don't impress for their own sake. Every entry must carry
two independent scores — **conv** (does it convert) and **wow** (does it
impress) — because awwwards-style sites are routinely art-over-conversion and a
library of orphaned prettiness is worthless to a build. An entry is only in the
library if it passes a bar: it converts well, or it wows *and* has something
concrete worth lifting. No "unreviewed" bucket. Vetted or it's not in.

## Section taxonomy (the `type` field)

Allowed values exactly:

| `type` | What it covers |
|---|---|
| `hero` | Above-fold headline + CTA + visual. Sub-types recorded in `styles` (product / typography-led / service / video-bg / full-bleed / split) |
| `bento` | Info grids, feature grids, bento boxes, bento grids |
| `social-proof` | Testimonials, reviews, logos, press mentions, ratings |
| `pricing` | Pricing cards, tiers, cost tellers |
| `faq` | FAQ / objection blocks |
| `how-it-works` | Steps, process, numbers-led workflows |
| `about` | Founder / about / story sections |
| `cta` | Final CTA, email capture, lead capture |
| `nav` | Header / navigation treatment |
| `3d` | 3D, WebGL, scroll-driven, interactive |
| `ecommerce` | Product pages, PDP layouts |
| `footer` | Footer treatments |

## Entry format (markdown block)

One entry = one markdown block in the library file, under the matching section
heading, in this exact shape:

```
### Name of the reference
- url: https://example.com
- type: hero
- styles: product, warm, high-contrast
- industry: any  (free-form tags, e.g. any / roofing / saas)
- source: out-of-geo | gallery | team
- borrow: <ONE concrete thing to lift, e.g. "massive layered headline, no card, phone visible above fold">
- why: <one line on why it works as a reference>
- conv: 8
- wow: 7
- shot: shots/foo.png   (omit if none)
- by: <agent/author that added it, e.g. Hermes / Claude-Code / human>
```

### Field rules (the append script enforces these)

- `url`, `type`, `borrow`, `conv`, `wow` are **required**. The script refuses
  anything missing them.
- `conv` and `wow` are integers 1-10. **10/10 is forbidden** — nothing is
  perfect — so the script caps at 9.
- `borrow` must be a **specific, concrete phrase** (a named element, an exact
  treatment). Vague praise like "nice modern layout" is rejected. Concretely:
  the script rejects `borrow` values under ~6 characters that contain only
  adverbs/adjectives and no noun. If it reads like "looks good / nice / clean /
  modern / beautiful" with nothing specific, it fails.
- `type` must be one of the taxonomy values above. Anything else is rejected.
- `source` should be `out-of-geo` (a competitor in another market), `gallery`
  (a design gallery / award site), or `team` (picked internally).
- `url` + `type` together must be unique across the whole library; a duplicate
  (url,type) pair is skipped. A single site can appear under several section
  types — a great hero AND a great FAQ from the same URL are both valid.

## Geographic rule (how to hunt references)

- **Never pull direct local competitors of the client.** A Detroit plumber does
  not get a Detroit plumber as a reference. Use the same industry in a different
  market (LA, Austin, Toronto) — same industry, no conflict, and those pages are
  usually conversion-optimized because they compete on leads.
- Cross-industry and award sites are fair game for the `wow` layer.
- `source: out-of-geo` marks the out-of-market competitors; `gallery` marks
  award / gallery finds.

## How to add an entry (any agent)

Do NOT hand-edit the library file by feel — run the script. It validates,
dedupes, and re-sorts by section so the file stays consistent no matter how many
agents touch it.

```bash
python3 references/append_reference.py file.json
# file.json = [{"url": "...", "type": "hero", ...}, ...]
# or a bare object for one entry
```

Less common flags: `--dry-run` prints what would be added without writing;
`--library /abs/path.md` points at a different library copy (for a local
checkout on another machine).

### JSON field names

Same as the markdown keys minus the `type:` prefix. `borrow`, `why`, `styles`,
`industry` are strings; `conv`, `wow` are ints; `shot`, `by`, `source`, `url`,
`type` as above. Unknown keys are dropped with a warning.

## Licensing the entries

References are for *inspiration* — borrow a layout idea, spacing, or a visual
treatment. Never copy another site's copy, images, or code wholesale. Keep this
in mind when you log and when you build.)
