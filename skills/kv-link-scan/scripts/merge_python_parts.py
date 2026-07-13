#!/usr/bin/env python3
"""Merge Python handbook chapters into Part volumes (Scheme A)."""
from __future__ import annotations

import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
TOPIC = VAULT / "Project" / "Python 生態系知識圖譜"

PARTS: list[tuple[str, str, str, list[str]]] = [
    ("0", "Part 0 · 導論", "Python/Part-0", [
        "0.1 · 導論 — 從韌體到 Python 生態系.md",
    ]),
    ("I", "Part I · 執行環境", "Python/Part-I", [
        "1.1 · Python 直譯器與執行模型.md",
        "1.2 · PATH 與環境變數.md",
        "1.3 · Site-packages 與 import 機制.md",
        "1.4 · ABI wheel 與二進位相容.md",
    ]),
    ("II", "Part II · 套件與隔離", "Python/Part-II", [
        "2.1 · 依賴地獄與隔離動機.md",
        "2.2 · Venv 與虛擬環境.md",
        "2.3 · Pip 與 PyPI 生態.md",
        "2.4 · Requirements 與鎖定策略.md",
        "2.5 · Pyproject.toml 與現代打包.md",
    ]),
    ("III", "Part III · 進階套件管理", "Python/Part-III", [
        "3.1 · Poetry 架構與工作流.md",
        "3.2 · Conda 架構與求解器.md",
        "3.3 · 套件管理決策樹.md",
    ]),
    ("IV", "Part IV · 專案工程", "Python/Part-IV", [
        "4.1 · Python 專案目錄結構.md",
        "4.2 · Git 與 Python 協作.md",
        "4.3 · VSCode Python 工作流.md",
    ]),
    ("V", "Part V · 部署", "Python/Part-V", [
        "5.1 · Docker 與 Python 容器化.md",
    ]),
    ("VI", "Part VI · AI 與科學計算", "Python/Part-VI", [
        "6.1 · CUDA 生態系.md",
        "6.2 · PyTorch 專案架構.md",
        "6.3 · OpenCV 與科學計算棧.md",
    ]),
    ("VII", "Part VII · 整合實戰", "Python/Part-VII", [
        "7.1 · 讀任意 GitHub 專案.md",
        "7.2 · 企業級 Python 工作流.md",
        "7.3 · 場景實戰案例集.md",
        "7.4 · 全域 FAQ 與錯誤診斷.md",
        "7.5 · 知識圖譜索引與學習路徑.md",
    ]),
]

PART_INTROS = {
    "Part 0 · 導論": "全書框架：怎麼讀、C/C++ 對照座標。",
    "Part I · 執行環境": "直譯器、PATH、import、ABI——「誰在跑 .py」。",
    "Part II · 套件與隔離": "venv、pip、lock、pyproject——依賴與隔離。",
    "Part III · 進階套件管理": "Poetry、Conda、決策樹——怎麼選工具。",
    "Part IV · 專案工程": "目錄結構、Git、IDE 工作流。",
    "Part V · 部署": "Docker 與 Python 容器化。",
    "Part VI · AI 與科學計算": "CUDA、PyTorch、OpenCV 棧。",
    "Part VII · 整合實戰": "讀 repo、企業流、場景、FAQ、學習路徑。",
}


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[: end + 4], text[end + 5 :].lstrip("\n")


def demote_headings(body: str) -> str:
    out: list[str] = []
    for line in body.splitlines():
        m = re.match(r"^(#{1,6})\s", line)
        if m:
            out.append("#" + line)
        else:
            out.append(line)
    return "\n".join(out)


def chapter_title_from_file(name: str) -> str:
    return name.removesuffix(".md")


def build_title_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for _pid, part_title, _tag, files in PARTS:
        for fname in files:
            ch = chapter_title_from_file(fname)
            mapping[ch] = f"{part_title}#{ch}"
    return mapping


def merge_parts() -> dict[str, str]:
    title_map = build_title_map()
    created_files: list[Path] = []

    for pid, part_title, part_tag, files in PARTS:
        out_name = f"{part_title}.md"
        out_path = TOPIC / out_name
        chapters: list[str] = []

        for fname in files:
            src = TOPIC / fname
            if not src.exists():
                raise FileNotFoundError(src)
            raw = src.read_text(encoding="utf-8")
            _fm, body = split_frontmatter(raw)
            chapters.append(demote_headings(body.strip()))

        fm = f"""---
title: {part_title}
parent: "[[Python 生態系知識圖譜 — MOC]]"
tags:
  - Python/Ecosystem
  - Python/Handbook
  - {part_tag}
part: "{pid}"
created: 2026-07-02
updated: 2026-07-06
---

# {part_title}

> **銜接**：[[Python 生態系知識圖譜 — MOC]]。{PART_INTROS.get(part_title, "")}

"""
        content = fm + "\n\n---\n\n".join(chapters) + "\n"
        out_path.write_text(content, encoding="utf-8")
        created_files.append(out_path)
        print(f"Wrote {out_path.name} ({len(files)} chapters)")

    return title_map


def replace_wikilinks(title_map: dict[str, str], roots: list[Path]) -> int:
    # longest titles first
    items = sorted(title_map.items(), key=lambda x: len(x[0]), reverse=True)
    count = 0
    for root in roots:
        for path in root.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            original = text
            for old, new_target in items:
                # [[title]] or [[title#anchor]] — only replace bare chapter links
                pattern = re.compile(
                    r"\[\[(?P<prefix>[^\]|#]*\|)?"
                    + re.escape(old)
                    + r"(?P<suffix>#[^\]]+)?\]\]"
                )

                def repl(m: re.Match[str], nt: str = new_target) -> str:
                    prefix = m.group("prefix") or ""
                    suffix = m.group("suffix") or ""
                    part_note = nt.split("#", 1)[0]
                    if suffix:
                        return f"[[{prefix}{part_note}{suffix}]]"
                    return f"[[{prefix}{nt}]]"

                text = pattern.sub(repl, text)
            if text != original:
                path.write_text(text, encoding="utf-8")
                count += 1
                print(f"Updated links: {path.relative_to(VAULT)}")
    return count


def delete_old_chapters() -> int:
    n = 0
    for _pid, _pt, _tag, files in PARTS:
        for fname in files:
            p = TOPIC / fname
            if p.exists():
                p.unlink()
                n += 1
                print(f"Deleted {fname}")
    return n


def main() -> None:
    title_map = merge_parts()
    replace_wikilinks(title_map, [VAULT / "Project"])
    n = delete_old_chapters()
    print(f"Done: 8 parts, {n} old chapters removed, link map {len(title_map)} entries")


if __name__ == "__main__":
    main()