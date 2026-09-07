#!/usr/bin/env python3
"""Prune weak / over-dense wikilinks; optionally fix Source/Image embeds (kv-link-scan)."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import scan_unlinked as scan  # noqa: E402

VAULT = scan.VAULT
UPDATED = "2026-08-19"
MAX_KEEP_PER_TARGET = 3
WIKILINK = re.compile(r"(!)?\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]")
FENCE = re.compile(r"```[\s\S]*?```")
IMAGE_DIR = VAULT / "Source" / "Image"


def protected_spans(body: str) -> set[int]:
    """Character offsets in 銜接 / 延伸 that must prefer keep."""
    prot: set[int] = set()
    for m in re.finditer(r"^> \*\*銜接\*\*.*(?:\n> .*)*", body, re.M):
        prot.update(range(m.start(), m.end()))
    for m in re.finditer(r"^## 延伸(?:閱讀)?\s*$", body, re.M):
        start = m.start()
        rest = body[m.end() :]
        nxt = re.search(r"\n## |\n---\n", rest)
        end = m.end() + (nxt.start() if nxt else len(rest))
        prot.update(range(start, end))
    return prot


def display_of(m: re.Match) -> str:
    return m.group(3) if m.group(3) else m.group(2).strip()


def prune_file(path: Path, fix_images: bool) -> dict:
    raw = path.read_text(encoding="utf-8")
    fm_m = re.match(r"^---\n.*?\n---\n", raw, re.DOTALL)
    fm = fm_m.group(0) if fm_m else ""
    body = raw[len(fm) :]
    self_title = path.stem
    stats = {"self": 0, "dup_line": 0, "over_repeat": 0, "images": 0}

    fences: list[str] = []

    def stash(m: re.Match) -> str:
        fences.append(m.group(0))
        return f"\x00F{len(fences)-1}\x00"

    work = FENCE.sub(stash, body)

    # 1) Image path fix
    if fix_images and IMAGE_DIR.is_dir():
        images = {p.name for p in IMAGE_DIR.iterdir() if p.is_file()}

        def img_fix(m: re.Match) -> str:
            bang, target, disp = m.group(1) or "", m.group(2).strip(), m.group(3)
            if target.startswith("Source/"):
                return m.group(0)
            base = target.split("/")[-1]
            if base in images:
                stats["images"] += 1
                pipe = f"|{disp}" if disp else ""
                return f"{bang}[[Source/Image/{base}{pipe}]]"
            return m.group(0)

        work = WIKILINK.sub(img_fix, work)

    # 2) Self-link + same-line dedupe (skip table rows for dedupe)
    lines = work.splitlines(keepends=True)
    new_lines: list[str] = []
    for line in lines:
        is_table = line.lstrip().startswith("|")

        def unself(m: re.Match) -> str:
            if m.group(1):
                return m.group(0)
            name = m.group(2).strip()
            if name == self_title:
                stats["self"] += 1
                return display_of(m)
            return m.group(0)

        line = WIKILINK.sub(unself, line)
        if is_table:
            new_lines.append(line)
            continue

        seen: set[str] = set()

        def dedup(m: re.Match) -> str:
            if m.group(1):
                return m.group(0)
            name = m.group(2).strip()
            if name.startswith("Source/"):
                return m.group(0)
            if name in seen:
                stats["dup_line"] += 1
                return display_of(m)
            seen.add(name)
            return m.group(0)

        new_lines.append(WIKILINK.sub(dedup, line))
    work = "".join(new_lines)

    # 3) Same-target over-repeat (keep ≤ MAX; prefer protected zones)
    prot = protected_spans(work)
    matches = [m for m in WIKILINK.finditer(work) if not m.group(1)]
    by_t: dict[str, list[re.Match]] = {}
    for m in matches:
        t = m.group(2).strip()
        if t.startswith("Source/"):
            continue
        by_t.setdefault(t, []).append(m)

    remove: list[tuple[int, int, str]] = []
    for _t, ms in by_t.items():
        if len(ms) <= MAX_KEEP_PER_TARGET:
            continue
        ranked = sorted(
            ms,
            key=lambda m: (
                0 if any(i in prot for i in range(m.start(), m.end())) else 1,
                m.start(),
            ),
        )
        keep_ids = {id(m) for m in ranked[:MAX_KEEP_PER_TARGET]}
        for m in ms:
            if id(m) not in keep_ids:
                remove.append((m.start(), m.end(), display_of(m)))
                stats["over_repeat"] += 1

    if remove:
        remove.sort(key=lambda x: x[0])
        parts: list[str] = []
        last = 0
        for s, e, disp in remove:
            parts.append(work[last:s])
            parts.append(disp)
            last = e
        parts.append(work[last:])
        work = "".join(parts)

    for i, f in enumerate(fences):
        work = work.replace(f"\x00F{i}\x00", f)

    total = stats["self"] + stats["dup_line"] + stats["over_repeat"] + stats["images"]
    if total == 0:
        return stats

    text = fm + work
    if "updated:" in text:
        text = re.sub(r"^updated:.*$", f"updated: {UPDATED}", text, flags=re.M)
    path.write_text(text, encoding="utf-8")
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="kv-link-scan prune weak links")
    parser.add_argument("--topic", help="Project subfolder name")
    parser.add_argument("--exclude", action="append", default=[])
    parser.add_argument(
        "--fix-images",
        action="store_true",
        help="Rewrite bare image wikilinks to Source/Image/…",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report only (not implemented as full dry-run; use scan first)",
    )
    args = parser.parse_args()
    if args.dry_run:
        print(json.dumps({"note": "use scan_unlinked.py for add candidates; prune is apply-only"}, ensure_ascii=False))
        return

    files = []
    totals = {"self": 0, "dup_line": 0, "over_repeat": 0, "images": 0}
    for path in scan.iter_targets(args.topic, args.exclude):
        st = prune_file(path, args.fix_images)
        n = sum(st.values())
        if n:
            files.append({"file": path.relative_to(VAULT).as_posix(), **st})
            for k in totals:
                totals[k] += st[k]

    # Also Architecture folder (single-file radar)
    arch = scan.PROJECT / "_Architecture"
    if arch.is_dir() and not args.topic:
        for path in arch.glob("*.md"):
            st = prune_file(path, args.fix_images)
            if sum(st.values()):
                files.append({"file": path.relative_to(VAULT).as_posix(), **st})
                for k in totals:
                    totals[k] += st[k]

    print(json.dumps({"totals": totals, "files": files}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
