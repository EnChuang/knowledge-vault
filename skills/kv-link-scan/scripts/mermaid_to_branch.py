#!/usr/bin/env python3
"""Convert ```mermaid flowchart/mindmap blocks to ```text branch diagrams."""
from __future__ import annotations

import re
import sys
from pathlib import Path

NODE_RE = re.compile(
    r"(\w+)\s*"
    r"(?:"
    r"\[\[([^\]]+)\]\]"
    r"|\[([^\]]+)\]"
    r"|\{([^}]+)\}"
    r"|\(\(([^)]+)\)\)"
    r")?"
)

MERMAID_BLOCK_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)


def parse_nodes(segment: str) -> dict[str, str]:
    labels: dict[str, str] = {}
    for m in NODE_RE.finditer(segment):
        nid = m.group(1)
        label = m.group(2) or m.group(3) or m.group(4) or m.group(5)
        if label:
            labels[nid] = label.strip()
        elif nid not in labels:
            labels[nid] = nid
    return labels


def parse_edges(line: str) -> list[tuple[str, str, str | None]]:
    """Return list of (src, dst, edge_label)."""
    line = line.strip()
    if "-->" not in line:
        return []

    labels = parse_nodes(line)
    # Tokenize by --> keeping optional |label|
    parts = re.split(r"\s*-->\s*", line)
    edges: list[tuple[str, str, str | None]] = []
    prev_id: str | None = None
    pending_label: str | None = None

    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        # Leading edge label from previous segment: |yes|
        label_match = re.match(r"^\|([^|]+)\|\s*(.+)$", part)
        if label_match and prev_id is None and i == 0:
            continue
        if part.startswith("|") and part.endswith("|") and i > 0:
            pending_label = part.strip("|").strip()
            continue

        # Extract node id at start of part (may have label suffix)
        nm = re.match(r"^(\w+)", part)
        if not nm:
            continue
        nid = nm.group(1)
        if nid in labels:
            pass
        else:
            labels[nid] = nid

        # Check if part starts with |label| node
        lm = re.match(r"^\|([^|]+)\|\s*(\w+)", part)
        if lm:
            pending_label = lm.group(1).strip()
            nid = lm.group(2)
            sub_labels = parse_nodes(part)
            labels.update(sub_labels)

        if prev_id is not None:
            edges.append((prev_id, nid, pending_label))
            pending_label = None
        prev_id = nid

    # Re-parse with simpler per-arrow regex for reliability
    edges.clear()
    labels.update(parse_nodes(line))
    pattern = re.compile(
        r"(\w+)\s*-->\s*(?:\|([^|]+)\|\s*)?(\w+)"
    )
    for m in pattern.finditer(line):
        src, elabel, dst = m.group(1), m.group(2), m.group(3)
        edges.append((src, dst, elabel.strip() if elabel else None))
    return edges


def parse_mermaid(body: str) -> tuple[str, dict[str, str], list[tuple[str, str, str | None]]]:
    lines = body.strip().splitlines()
    direction = "TD"
    labels: dict[str, str] = {}
    edges: list[tuple[str, str, str | None]] = []

    if lines and lines[0].strip().startswith("mindmap"):
        return "mindmap", labels, edges

    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("flowchart") or s.startswith("graph"):
            for d in ("LR", "RL", "TB", "BT", "TD"):
                if d in s.upper():
                    direction = d
            continue
        labels.update(parse_nodes(s))
        edges.extend(parse_edges(s))

    for src, dst, _ in edges:
        labels.setdefault(src, src)
        labels.setdefault(dst, dst)

    return direction, labels, edges


def children_map(
    edges: list[tuple[str, str, str | None]],
) -> dict[str, list[tuple[str | None, str]]]:
    cmap: dict[str, list[tuple[str | None, str]]] = {}
    for src, dst, elabel in edges:
        cmap.setdefault(src, []).append((elabel, dst))
    return cmap


def roots(edges: list[tuple[str, str, str | None]], labels: dict[str, str]) -> list[str]:
    incoming = {dst for _, dst, _ in edges}
    all_nodes = set(labels) | {s for s, _, _ in edges} | {d for _, d, _ in edges}
    r = [n for n in all_nodes if n not in incoming]
    return sorted(r, key=lambda x: labels.get(x, x))


def fmt_node(nid: str, labels: dict[str, str]) -> str:
    return labels.get(nid, nid)


def render_tree(
    node: str,
    cmap: dict[str, list[tuple[str | None, str]]],
    labels: dict[str, str],
    prefix: str = "",
    is_last: bool = True,
    visited: set[str] | None = None,
) -> list[str]:
    if visited is None:
        visited = set()
    lines: list[str] = []
    connector = "└── " if is_last else "├── "
    if prefix:
        text = fmt_node(node, labels)
        lines.append(f"{prefix}{connector}{text}")
        child_prefix = prefix + ("    " if is_last else "│   ")
    else:
        lines.append(fmt_node(node, labels))
        child_prefix = ""

    if node in visited:
        lines[-1] = lines[-1] + "（↩ 見上）"
        return lines
    visited = visited | {node}

    kids = cmap.get(node, [])
    for i, (elabel, child) in enumerate(kids):
        last = i == len(kids) - 1
        branch = "└── " if last else "├── "
        label_text = f"{elabel} → " if elabel else ""
        lines.append(f"{child_prefix}{branch}{label_text}{fmt_node(child, labels)}")
        sub = render_tree(child, cmap, labels, child_prefix, last, visited)
        # sub includes duplicate root; skip first line
        if len(sub) > 1:
            lines.extend(sub[1:])
    return lines


def render_lr_chain(
    edges: list[tuple[str, str, str | None]], labels: dict[str, str]
) -> list[str]:
    cmap = children_map(edges)
    rs = roots(edges, labels)
    lines: list[str] = []
    for root in rs:
        chain = [fmt_node(root, labels)]
        cur = root
        seen = {cur}
        while cur in cmap and len(cmap[cur]) == 1:
            elabel, nxt = cmap[cur][0]
            part = fmt_node(nxt, labels)
            if elabel:
                part = f"{elabel} → {part}"
            chain.append(part)
            if nxt in seen:
                break
            seen.add(nxt)
            cur = nxt
        lines.append(" → ".join(chain))
        # branches off the chain
        for node in seen:
            kids = cmap.get(node, [])
            if len(kids) > 1:
                lines.append(f"{fmt_node(node, labels)} 分支：")
                for elabel, child in kids[1:]:
                    sub = " → ".join(
                        [fmt_node(child, labels)]
                        + [
                            fmt_node(d, labels)
                            for _, d in cmap.get(child, [])[:3]
                        ]
                    )
                    tag = f"{elabel} → " if elabel else ""
                    lines.append(f"  · {tag}{sub}")
            elif len(kids) == 1 and kids[0][1] not in seen:
                elabel, child = kids[0]
                tag = f"{elabel} → " if elabel else ""
                lines.append(f"  · {fmt_node(node, labels)} ──{tag}► {fmt_node(child, labels)}")
    return lines or ["（空圖）"]


def render_mindmap(body: str) -> list[str]:
    lines = body.strip().splitlines()[1:]  # skip mindmap
    result = ["Python 生態系"]
    for line in lines:
        s = line.strip()
        if not s or s.startswith("root"):
            continue
        indent = len(line) - len(line.lstrip())
        depth = indent // 2
        prefix = "  " * depth + ("├── " if depth else "")
        text = s.replace("Part", "Part ")
        result.append(f"{prefix}{text}")
    return result


def convert_block(body: str) -> str:
    direction, labels, edges = parse_mermaid(body)
    if direction == "mindmap":
        out_lines = render_mindmap(body)
    elif direction in ("LR", "RL"):
        out_lines = render_lr_chain(edges, labels)
    else:
        cmap = children_map(edges)
        rs = roots(edges, labels)
        out_lines: list[str] = []
        for i, root in enumerate(rs):
            if i:
                out_lines.append("")
            out_lines.extend(render_tree(root, cmap, labels))
        if not out_lines:
            out_lines = ["（空圖）"]
    return "```text\n" + "\n".join(out_lines) + "\n```"


def convert_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return convert_block(m.group(1))

    new_text = MERMAID_BLOCK_RE.sub(repl, text)
    if count:
        path.write_text(new_text, encoding="utf-8")
    return count


def collect_targets(vault: Path, args: list[str]) -> list[Path]:
    if not args:
        return list((vault / "Project").rglob("*.md"))
    out: list[Path] = []
    for raw in args:
        p = Path(raw)
        if not p.is_absolute():
            p = vault / p
        if p.is_dir():
            out.extend(p.rglob("*.md"))
        elif p.exists():
            out.append(p)
    return out


def main(argv: list[str]) -> int:
    vault = Path(__file__).resolve().parents[3]
    targets = collect_targets(vault, argv[1:])
    total = 0
    files = 0
    for path in sorted(set(targets)):
        if not path.is_file():
            continue
        n = convert_file(path)
        if n:
            files += 1
            total += n
            print(f"{path.relative_to(vault)}: {n} block(s)")
    print(f"Done: {total} block(s) in {files} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))