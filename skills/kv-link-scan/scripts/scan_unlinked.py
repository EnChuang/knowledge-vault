#!/usr/bin/env python3
"""Scan Project notes for unlinked knowledge node mentions (kv-link-scan)."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
PROJECT = VAULT / "Project"
SKIP_DIRS_DEFAULT = {"_DailyChange"}
MOC_SUFFIX = " — MOC.md"
HIGH_FREQ = ["AI Agent 工程", "MEMORY", "DailyChange", "Architecture-Status"]
# Auto-add skip: short / common-noun false positives
DENY_AUTO_ADD = {"MOC", "Session"}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
FENCE_RE = re.compile(r"```[\s\S]*?```|````[\s\S]*?````")

ZONE_MARKERS = [
    (re.compile(r"^> \*\*銜接\*\*", re.M), "章首銜接"),
    (re.compile(r"^\| \*\*前置知識\*\* \|", re.M), "章首表"),
    (re.compile(r"^\| \*\*後續章節\*\* \|", re.M), "章首表"),
    (re.compile(r"^## 5 Relationship Diagram", re.M), "§5"),
    (re.compile(r"^## 14 Further Reading", re.M), "§14"),
    (re.compile(r"^## 延伸閱讀", re.M), "延伸閱讀"),
    (re.compile(r"^## 延伸\s*$", re.M), "延伸"),
    (re.compile(r"^## 專題簡介", re.M), "MOC簡介"),
]


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def extract_moc_links(text: str) -> list[str]:
    out: list[str] = []
    for m in WIKILINK_RE.finditer(text):
        name = m.group(1).strip()
        if name.startswith("Source/"):
            continue
        out.append(name)
    return out


def skip_dirs(extra: list[str] | None) -> set[str]:
    s = set(SKIP_DIRS_DEFAULT)
    if extra:
        s.update(extra)
    return s


def collect_nodes(topic: str | None, exclude: list[str] | None = None) -> list[str]:
    nodes: set[str] = set(HIGH_FREQ)
    skip = skip_dirs(exclude)
    topics = [PROJECT / topic] if topic else [p for p in PROJECT.iterdir() if p.is_dir()]

    for topic_dir in topics:
        if topic_dir.name in skip:
            continue
        for path in topic_dir.glob("*.md"):
            if path.name.endswith(MOC_SUFFIX):
                text = path.read_text(encoding="utf-8")
                nodes.update(extract_moc_links(text))
                alias_block = re.search(
                    r"^aliases:\s*\n((?:\s+-\s+.+\n)+)", text, re.M
                )
                if alias_block:
                    for line in alias_block.group(1).splitlines():
                        m = re.match(r"\s+-\s+(.+)", line)
                        if m:
                            nodes.add(m.group(1).strip())
            else:
                nodes.add(path.stem)

    # Resolve existing note stems (any Project topic, for existence check)
    existing: set[str] = set()
    for d in PROJECT.iterdir():
        if not d.is_dir() or d.name in skip_dirs(exclude):
            continue
        for p in d.glob("*.md"):
            existing.add(p.stem)
        # _Architecture
    arch = PROJECT / "_Architecture"
    if arch.is_dir():
        for p in arch.glob("*.md"):
            existing.add(p.stem)
    # Vault-root notes sometimes linked (DailyChange lives under _DailyChange)
    dc = PROJECT / "_DailyChange" / "DailyChange.md"
    if dc.is_file():
        existing.add("DailyChange")
    for root_name in ("MEMORY", "AGENTS", "Architecture-Status"):
        pass
    if (VAULT / "MEMORY.md").is_file():
        existing.add("MEMORY")

    cleaned = []
    for n in nodes:
        if len(n) < 3:
            continue
        if n in DENY_AUTO_ADD:
            continue
        if "/" in n and re.match(r"^[\w\-]+/[\w\-]+", n):
            continue
        # Only auto-suggest nodes that resolve to a real .md (or allowlisted HF that exist)
        if n not in existing:
            continue
        cleaned.append(n)
    return sorted(set(cleaned), key=len, reverse=True)


def linked_nodes(text: str) -> set[str]:
    return {m.group(1).strip() for m in WIKILINK_RE.finditer(text)}


def zone_spans(text: str) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    for pattern, label in ZONE_MARKERS:
        for m in pattern.finditer(text):
            start = m.start()
            rest = text[start:]
            nxt = re.search(r"\n## |\n---\n", rest[1:])
            end = start + (1 + nxt.start()) if nxt else len(text)
            spans.append((start, end, label))
    if not spans:
        return []
    spans.sort(key=lambda x: x[0])
    merged: list[tuple[int, int, str]] = []
    for s, e, lbl in spans:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e), merged[-1][2] + "+" + lbl)
        else:
            merged.append((s, e, lbl))
    return merged


def scan_file(path: Path, nodes: list[str], self_title: str) -> list[dict]:
    raw = path.read_text(encoding="utf-8")
    body = strip_frontmatter(raw)
    linked = linked_nodes(body)
    zones = zone_spans(body)
    if not zones:
        return []

    findings: list[dict] = []
    for start, end, zone in zones:
        segment = body[start:end]
        seg_offset = start
        masked = FENCE_RE.sub(lambda m: " " * len(m.group(0)), segment)
        for node in nodes:
            if node == self_title or node in linked:
                continue
            if len(node) < 3:
                continue
            for m in re.finditer(re.escape(node), masked):
                abs_pos = seg_offset + m.start()
                before = body[max(0, abs_pos - 2) : abs_pos]
                after = body[abs_pos + len(node) : abs_pos + len(node) + 2]
                if before.endswith("[") or after.startswith("]"):
                    continue
                snippet = body[max(0, abs_pos - 20) : abs_pos + len(node) + 20].replace("\n", " ")
                findings.append(
                    {
                        "file": path.relative_to(VAULT).as_posix(),
                        "zone": zone,
                        "node": node,
                        "snippet": snippet,
                    }
                )
                break
    return findings


def iter_targets(topic: str | None, exclude: list[str] | None = None) -> list[Path]:
    paths: list[Path] = []
    skip = skip_dirs(exclude)
    dirs = [PROJECT / topic] if topic else [p for p in PROJECT.iterdir() if p.is_dir()]
    for d in dirs:
        if d.name in skip:
            continue
        paths.extend(sorted(d.glob("*.md")))
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description="kv-link-scan unlinked node report")
    parser.add_argument("--topic", help="Project subfolder name")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Extra Project subfolder to skip (repeatable), e.g. --exclude \"life update\"",
    )
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    nodes = collect_nodes(args.topic, args.exclude)
    all_findings: list[dict] = []
    for path in iter_targets(args.topic, args.exclude):
        all_findings.extend(scan_file(path, nodes, path.stem))

    if args.json:
        print(
            json.dumps(
                {
                    "nodes": len(nodes),
                    "exclude": sorted(skip_dirs(args.exclude)),
                    "findings": all_findings,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    print("# kv-link-scan 報告\n")
    print(f"- 範圍：{args.topic or '全庫 Project（頂層專題）'}")
    print(f"- 排除：{', '.join(sorted(skip_dirs(args.exclude)))}")
    print(f"- 詞彙節點數：{len(nodes)}")
    print(f"- 候選總數：{len(all_findings)}\n")
    if not all_findings:
        print("（白名單區段內無未連結候選）")
        return
    print("| 檔案 | 區段 | 建議連結 | 片段 |")
    print("|------|------|----------|------|")
    for f in all_findings[:200]:
        snip = f["snippet"].replace("|", "\\|")[:60]
        print(f"| {f['file']} | {f['zone']} | [[{f['node']}]] | …{snip}… |")
    if len(all_findings) > 200:
        print(f"\n（其餘 {len(all_findings) - 200} 筆略）")


if __name__ == "__main__":
    main()

