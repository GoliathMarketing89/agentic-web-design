#!/usr/bin/env python3
"""
Append design references to the Goliath web-design reference library.

Any agent can add to the library safely by passing JSON on stdin or a file.
The script validates the contract (required fields, taxonomy `type`, score
bounds, concrete `borrow`), dedupes by URL, and re-sorts by section so the
file stays consistent no matter how many agents write to it.

Usage:
    python3 append_reference.py entry.json              # one entry / a list
    python3 append_reference.py --dry-run entry.json    # validate only
    python3 append_reference.py --library PATH entry.json  # different copy
    cat entries.ndjson | python3 append_reference.py    # read from stdin
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---- the contract values (must match reference-spec.md) -------------------
HERE = Path(__file__).resolve().parent
DEFAULT_LIBRARY = HERE / "design-reference-library.md"

VALID_TYPES = {
    "hero", "bento", "social-proof", "pricing", "faq", "how-it-works",
    "about", "cta", "nav", "3d", "ecommerce", "footer",
}
VALID_SOURCES = {"out-of-geo", "gallery", "team"}
REQUIRED_KEYS = {"url", "type", "borrow", "conv", "wow"}
INT_KEYS = {"conv", "wow"}
STR_KEYS = {"name", "url", "type", "styles", "industry", "source", "borrow", "why", "shot", "by"}

# Specific-vs-vague `borrow` guardrail from the spec. Regex can't judge taste,
# but it can catch the worst offenders: a borrow made only of generic adjectives
# plus at most a generic container noun (layout/section/page/site/design) is
# necessarily vague — it names no concrete element or treatment.
_SPECIFIC_NOUNS = re.compile(
    r"\b(headline|hero|card|card-grid|grid|bento|nav|navbar|menu|footer|button|cta|"
    r"typography|typeface|spacing|negative space|overlay|gradient|image|photo|video|"
    r"marquee|divider|hairline|pill|tabs|accordion|carousel|testimonial|pricing|"
    r"sidebar|component|feature|form|input|toggle|badge|icon|"
    r"pull-quote|pullquote|hero-layout|stacked|layered)\b",
    re.IGNORECASE,
)
# generic approval adjectives that, alone or in a short cluster, add nothing
_GENERIC_ADJ = re.compile(
    r"\b(nice|clean|modern|beautiful|good|cool|great|professional|slick|sleek|elegant|"
    r"premium|minimal|simple|fresh|polished|attractive)\b",
    re.IGNORECASE,
)


def _is_vague_borrow(borrow: str) -> bool:
    """True when the borrow names no concrete element beyond a generic container."""
    b = borrow.strip()
    if len(b) < 6:
        return True
    # If it names a specific element, we trust it — even with adjectives around.
    if _SPECIFIC_NOUNS.search(b):
        return False
    # Otherwise: if it's mostly adjectives + filler and nothing concrete, vague.
    return bool(_GENERIC_ADJ.search(b))


def parse_input(raw: str) -> list[dict]:
    """Accept a single JSON object or a JSON array; also line-delimited JSON."""
    raw = raw.strip()
    if not raw:
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # try NDJSON
        entries = []
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line: {line!r} ({e})")
        return entries
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        return data
    raise ValueError("Input must be a JSON object or array of objects")


def normalize(entry: dict) -> tuple[list[str], dict]:
    """Validate one entry; return (errors, normalized_entry)."""
    errors = []
    out = {}

    for k in REQUIRED_KEYS:
        if k not in entry or entry[k] in (None, ""):
            errors.append(f"missing required field: {k}")

    for k in INT_KEYS:
        if k in entry and entry[k] is not None:
            try:
                v = int(entry[k])
            except (TypeError, ValueError):
                errors.append(f"{k} must be an integer, got {entry[k]!r}")
                continue
            if v > 9:
                out["_notes"] = out.get("_notes", []) + [
                    f"{k}:{v} capped to 9 (10 is forbidden by spec)"
                ]
            v = max(1, min(9, v))  # 1-9 hard cap; 10 forbidden
            out[k] = v

    for k in STR_KEYS:
        if k in entry and entry[k] is not None:
            out[k] = str(entry[k]).strip()

    if "type" in out and out["type"] not in VALID_TYPES:
        errors.append(
            f"invalid type {out['type']!r}; allowed: {', '.join(sorted(VALID_TYPES))}"
        )
    if "source" in out and out["source"] not in VALID_SOURCES:
        errors.append(
            f"invalid source {out['source']!r}; allowed: {', '.join(sorted(VALID_SOURCES))}"
        )
    if "borrow" in out:
        b = out["borrow"]
        if len(b) < 6:
            errors.append("borrow must be a concrete phrase (>= 6 chars)")
        elif _is_vague_borrow(b):
            errors.append(
                f"borrow is too vague: {b!r} — name a specific element/treatment, not an adjective"
            )

    url = out.get("url")
    if url and not url.startswith(("http://", "https://")):
        errors.append(f"url must start with http(s), got {url!r}")

    return errors, out


def to_block(e: dict) -> str:
    lines = [f"### {e.get('name', e['url'])}"]
    for k in ("name", "url", "type", "styles", "industry", "source", "borrow", "why", "conv", "wow", "shot", "by"):
        if k in e:
            lines.append(f"- {k}: {e[k]}")
    return "\n".join(lines)


def parse_blocks(text: str) -> list[dict]:
    """Read existing library file back into structured entries."""
    entries = []
    current = None
    for line in text.splitlines():
        m = re.match(r"^###\s+(.*)", line)
        if m:
            if current:
                entries.append(current)
            current = {"_name": m.group(1)}
        elif current is not None:
            fm = re.match(r"^-\s*([a-z0-9_-]+):\s*(.*)$", line)
            if fm:
                key, val = fm.group(1), fm.group(2)
                if key in INT_KEYS:
                    try:
                        current[key] = int(val)
                    except ValueError:
                        current[key] = val
                else:
                    current[key] = val
    if current:
        entries.append(current)
    return entries


def dedupe_key(e: dict) -> tuple[str, str] | None:
    """Unique identity of an entry: (url, type). A single site legitimately
    belongs under multiple section types (great hero AND great FAQ), so URL
    alone is too coarse to dedupe on."""
    url = e.get("url")
    if not url:
        return None
    return (url, e.get("type", ""))


def rebuild(entries: list[dict]) -> str:
    """Group entries by type in the canonical section order and render md."""
    order = [
        "hero", "bento", "social-proof", "pricing", "faq", "how-it-works",
        "about", "cta", "nav", "3d", "ecommerce", "footer",
    ]
    by_type = {}
    for e in entries:
        by_type.setdefault(e.get("type", "?") , []).append(e)

    out = []
    for t in order:
        group = by_type.pop(t, [])
        if group:
            out.append(f"## {t}")
            for e in sorted(group, key=lambda x: x.get("_name", "").lower()):
                out.append(to_block(e))
                out.append("")
    # anything with a type we no longer recognise (shouldn't happen) appended:
    for t in sorted(by_type):
        for e in by_type[t]:
            out.append(to_block(e))
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", nargs="?", help="path to JSON file (or pipe json to stdin)")
    ap.add_argument("--dry-run", action="store_true", help="validate only, don't write")
    ap.add_argument("--library", default=str(DEFAULT_LIBRARY), help="path to library file")
    args = ap.parse_args()

    if args.input:
        raw = Path(args.input).read_text(encoding="utf-8")
    else:
        raw = sys.stdin.read()

    entries = parse_input(raw)
    if not entries:
        print("No entries provided.")
        sys.exit(1)

    errors_total = []
    norm = []
    for e in entries:
        errors, out = normalize(e)
        if errors:
            for err in errors:
                errors_total.append(f"  [{e.get('url', '?')}] {err}")
        else:
            norm.append(out)

    if errors_total:
        print("FAILED — validation errors (nothing written):")
        print("\n".join(errors_total))
        sys.exit(1)

    lib = Path(args.library)
    existing = parse_blocks(lib.read_text(encoding="utf-8")) if lib.exists() else []
    seen = {dedupe_key(e) for e in existing}

    added, skipped = [], []
    for e in norm:
        key = dedupe_key(e)
        if key in seen:
            reason = f"url already logged for type '{e.get('type')}'"
            skipped.append(f"{e['url']} ({reason})")
            continue
        existing.append(e)
        seen.add(key)
        added.append(e["url"])
        for note in e.get("_notes", []):
            print(f"  NOTE [{e['url']}]: {note}")

    if args.dry_run:
        print(f"OK — {len(added)} would be added, {len(skipped)} duplicates skipped")
        for a in added:
            print(f"  + {a}")
        sys.exit(0)

    lib.write_text(rebuild(existing), encoding="utf-8")
    print(f"Wrote {len(added)} new reference(s) to {lib}")
    for a in added:
        print(f"  + {a}")
    if skipped:
        print(f"Skipped {len(skipped)} duplicate(s): {', '.join(skipped)}")


if __name__ == "__main__":
    main()
