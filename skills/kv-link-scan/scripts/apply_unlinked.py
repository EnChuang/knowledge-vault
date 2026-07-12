#!/usr/bin/env python3
"""Apply wikilinks from kv-link-scan findings (whitelist zones only)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# import scan module from same directory
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import scan_unlinked as scan  # noqa: E402

VAULT = scan.VAULT
UPDATED = "2026-07-02"
MAX_PER_SEGMENT = 2


def longest_node_at(segment: str, pos: int, nodes: list[str]) -> str | None:
    best: str | None = None
    for node in nodes:
        if segment[pos : pos + len(node)] == node:
            if best is None or len(node) > len(best):
                best = node
    return best


def link_once(segment: str, nodes: list[str], linked: set[str]) -> tuple[str, int]:
    i = 0
    while i < len(segment):
        if segment.startswith("[[", i):
            close = segment.find("]]", i + 2)
            i = close + 2 if close != -1 else i + 1
            continue
        node = longest_node_at(segment, i, nodes)
        if node and node not in linked:
            return segment[:i] + f"[[{node}]]" + segment[i + len(node) :], 1
        i += 1
    return segment, 0


def apply_file(path: Path, nodes: list[str]) -> int:
    raw = path.read_text(encoding="utf-8")
    body = scan.strip_frontmatter(raw)
    fm_match = re.match(r"^---\n.*?\n---\n", raw, re.DOTALL)
    fm = fm_match.group(0) if fm_match else ""
    self_title = path.stem
    linked = scan.linked_nodes(body)
    zones = scan.zone_spans(body)
    if not zones:
        return 0

    total = 0
    new_body = body
    offset_shift = 0
    for start, end, _zone in zones:
        s = start + offset_shift
        e = end + offset_shift
        segment = new_body[s:e]
        seg_linked = scan.linked_nodes(segment)
        count_in_seg = len(seg_linked)
        pool = [n for n in nodes if n != self_title]
        while count_in_seg < MAX_PER_SEGMENT:
            segment, n = link_once(segment, pool, seg_linked | linked)
            if not n:
                break
            count_in_seg += 1
            total += n
            for node in pool:
                if f"[[{node}]]" in segment:
                    seg_linked.add(node)
                    linked.add(node)
        new_body = new_body[:s] + segment + new_body[e:]
        offset_shift += len(segment) - (e - s)

    if total == 0:
        return 0
    text = fm + new_body
    if "updated:" in text:
        text = re.sub(r"^updated:.*$", f"updated: {UPDATED}", text, flags=re.M)
    path.write_text(text, encoding="utf-8")
    return total


def main() -> None:
    topic = None
    if len(sys.argv) > 2 and sys.argv[1] == "--topic":
        topic = sys.argv[2]
    nodes = scan.collect_nodes(topic)
    grand = 0
    touched: list[str] = []
    for path in scan.iter_targets(topic):
        n = apply_file(path, nodes)
        if n:
            grand += n
            touched.append(f"{path.relative_to(VAULT).as_posix()}: {n}")
    print(json.dumps({"links_added": grand, "files": touched}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()