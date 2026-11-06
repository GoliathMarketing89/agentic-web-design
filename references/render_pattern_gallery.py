#!/usr/bin/env python3
"""Render the observed-pattern JSON catalogs into a visual gallery and agent notes.

Run from any directory: python references/render_pattern_gallery.py
The JSON catalogs are the source of truth; generated files are read-only outputs.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = [
    ("fit", "Use when"), ("avoid", "Avoid when"), ("slots", "Content slots"),
    ("composition", "Desktop composition"), ("mobile_behavior", "Observed mobile behavior"),
    ("rebuild", "Rebuild recipe"), ("assets", "Asset production"),
    ("adapt", "Adaptation decisions"), ("interaction", "Interaction evidence and gaps"),
    ("verification", "Verification"),
]


def main():
    entries = []
    for catalog in sorted((ROOT / "patterns").glob("*.json")):
        entries.extend(json.loads(catalog.read_text(encoding="utf-8")))
    ids = set()
    for entry in entries:
        if entry["id"] in ids:
            raise ValueError(f"Duplicate pattern ID: {entry['id']}")
        ids.add(entry["id"])
        for group in ("desktop", "mobile"):
            if not entry[group]:
                raise ValueError(f"Missing {group} evidence: {entry['id']}")
            for shot in entry[group]:
                path = (ROOT / shot).resolve()
                if not path.is_relative_to(ROOT) or not path.is_file():
                    raise ValueError(f"Invalid screenshot path: {shot}")
        for key, _ in FIELDS:
            if not entry[key].strip():
                raise ValueError(f"Missing {key}: {entry['id']}")

    esc = html.escape
    cards = []
    notes = ["# Observed hero and bento references", "",
             "Generated from `patterns/*.json` by `render_pattern_gallery.py`.", "",
             "Screenshots are reference evidence, not reusable client assets. Scores describe editorial judgments of visual impact and conversion clarity, not measured performance. Observed references have not been validated through a complete rebuild.", ""]
    for kind in ("hero", "bento"):
        cards.append(f'<h2 class="group" id="{kind}">{kind.title()} sections</h2>')
        for e in (v for v in entries if v["type"] == kind):
            media = []
            for group in ("desktop", "mobile"):
                images = ''.join(
                    f'<a href="{esc(s)}"><img loading="lazy" src="{esc(s)}" alt="{esc(e["name"])} — {group} view {i+1}"></a>'
                    for i, s in enumerate(e[group]))
                media.append(f'<details {"open" if group == "desktop" else ""}><summary>{group.title()} evidence · {len(e[group])} view(s)</summary><div class="screens {group}">{images}</div></details>')
            details = ''.join(f'<h4>{label}</h4><p>{esc(e[key])}</p>' for key, label in FIELDS)
            cards.append(
                f'<article id="{esc(e["id"])}"><div class="label">{esc(e["styles"])}</div>'
                f'<h3>{esc(e["name"])}</h3><p>{esc(e["why"])}</p>'
                f'<p class="meta">Observed {esc(e["observed"])} · clarity {e["conv"]}/9 · visual impact {e["wow"]}/9</p>'
                f'<p class="meta">{esc(e["status"])}</p><a href="{esc(e["url"])}" target="_blank" rel="noreferrer">Visit original ↗</a>'
                + ''.join(media) + f'<details><summary>Rebuild and adapt</summary>{details}</details></article>')
            notes.extend([f'## {e["name"]}', "", f'ID: `{e["id"]}` · Type: {e["type"]} · Observed: {e["observed"]}', "",
                          f'Source: [{e["name"]}]({e["url"]})', "", f'Status: {e["status"]}.', "",
                          f'Borrow: {e["borrow"]}', "",
                          f'Editorial scores: conversion clarity {e["conv"]}/9; visual impact {e["wow"]}/9. No measured uplift.', ""])
            for group in ("desktop", "mobile"):
                notes.append(group.title()+': '+', '.join(f'[view {i+1}]({s})' for i,s in enumerate(e[group])))
                notes.append("")
            for key, label in FIELDS:
                notes.extend([f'### {label}', "", e[key], ""])
    style = """
*{box-sizing:border-box}body{margin:0;background:#f4f2ee;color:#232323;font:16px/1.55 system-ui,sans-serif}
header,main,footer{max-width:1440px;margin:auto;padding:32px}header{padding-top:64px}h1{font-size:clamp(32px,5vw,64px);line-height:1.05;letter-spacing:-.05em;margin:16px 0}header p{max-width:820px;color:#555}
nav{display:flex;gap:24px}a{color:inherit;text-underline-offset:3px}main{display:grid;grid-template-columns:1fr 1fr;gap:28px}.group{grid-column:1/-1;font-size:28px;margin:40px 0 0}
article{background:white;border:1px solid #d7d4ce;padding:24px;min-width:0;scroll-margin-top:20px}h3{font-size:24px;line-height:1.2;margin:12px 0}.label,.meta{font-size:12px;color:#666}.label{text-transform:uppercase;letter-spacing:.06em}h4{margin:24px 0 6px}p{margin:10px 0}details{margin-top:20px;border-top:1px solid #ddd;padding-top:12px}summary{cursor:pointer;font-weight:600}.screens{display:flex;gap:10px;overflow:auto;padding-top:16px;align-items:flex-start}.screens a{display:block;min-width:100%;flex:0 0 100%}.screens img{width:100%;height:auto;display:block;border:1px solid #ddd}.mobile a{min-width:45%;flex-basis:45%}footer{color:#555;font-size:14px}
@media(max-width:800px){main{grid-template-columns:1fr}header,main,footer{padding:20px}article{padding:16px}}
"""
    page = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Goliath — real section references</title><style>{style}</style>
<header><div class="label">Goliath / observed references / first collection</div><h1>Real sections.<br>Ideas you can rebuild.</h1><p>Six inspected hero and bento sections with desktop and mobile evidence, content requirements, asset direction, and adaptation recipes. Images belong to their original creators. These references guide a new design; they are not a stock-asset library.</p><nav><a href="#hero">Heroes</a><a href="#bento">Bento layouts</a><a href="rebuild-notes.md">Agent notes</a></nav></header><main>{''.join(cards)}</main><footer>Clarity and visual-impact scores are editorial judgments, not measured conversion results. Each example is observed, not rebuild-validated. Click an image for its original capture; additional views scroll horizontally.</footer></html>'''
    (ROOT / "pattern-gallery.html").write_text(page, encoding="utf-8")
    (ROOT / "rebuild-notes.md").write_text('\n'.join(notes), encoding="utf-8")
    print(f"Rendered {len(entries)} patterns with verified screenshot paths")


if __name__ == "__main__":
    main()
