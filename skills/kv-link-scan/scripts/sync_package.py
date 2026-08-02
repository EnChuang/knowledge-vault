#!/usr/bin/env python3
"""Sync library root AGENTS, Bootstrap, skills/kv-* to .grok/skills/ and 建庫開箱（打包用）.

MEMORY.md and DailyChange in the open-box package are always blank seeds
(never copy private vault session data).
"""
from __future__ import annotations

import shutil
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
PKG = VAULT / "建庫開箱（打包用）" / "建庫開箱（打包用）"
GROK_SKILLS = VAULT / ".grok" / "skills"
SKILLS_SRC = VAULT / "skills"

BLANK_MEMORY = """---
title: MEMORY
tags:
  - 方法論/Memory
updated: {today}
---

#M2 u={yymmdd} s=v18

[HOT]
act=-
pref=ebook§12,fmt:$$+m+10q+ax,lfull>dc,pause>ask
open=-
ptr=s18,arch,dc

[LOG]
"""

BLANK_DAILY = """---
title: DailyChange
tags:
  - 方法論/DailyChange
created: 2026-07-02
updated: {today}
---

# DailyChange

> **當期變更日誌**（人類可讀）。本夾僅此一檔；每次**完整交付審查**後覆寫「當期」區。Session 交班（僅 AI）→ 庫根 `MEMORY.md`。

---

## 當期（最新一輪完整交付審查）

（尚無內容。首次完整交付審查後覆寫本區。）

---

## 開放風險（跨任務，仍有效才留）

| 項 | 來源 | 狀態 |
|----|------|------|

---

## 淘汰摘要（每任務一行，滿 15 行刪最舊）

| 日期 | 任務 | Verdict | 淘汰理由 |
|------|------|---------|----------|
"""


def copy_skill_tree(skill_dir: Path, dst_root: Path) -> None:
    dst = dst_root / skill_dir.name
    for src_file in skill_dir.rglob("*"):
        if src_file.is_dir() or "__pycache__" in src_file.parts:
            continue
        if src_file.suffix == ".pyc":
            continue
        rel = src_file.relative_to(skill_dir)
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, out)


def write_blank_package_seeds() -> None:
    today = date.today().isoformat()
    yymmdd = date.today().strftime("%y%m%d")
    mem = PKG / "MEMORY.md"
    mem.write_text(
        BLANK_MEMORY.format(today=today, yymmdd=yymmdd),
        encoding="utf-8",
    )
    dc = PKG / "Project" / "_DailyChange" / "DailyChange.md"
    dc.parent.mkdir(parents=True, exist_ok=True)
    dc.write_text(BLANK_DAILY.format(today=today), encoding="utf-8")


for name in ("AGENTS.md", "Bootstrap.md"):
    src = VAULT / name
    if src.exists():
        shutil.copy2(src, PKG / name)

# Do NOT copy vault MEMORY.md or private DailyChange into the open-box package.
write_blank_package_seeds()

skill_dirs = sorted(p for p in SKILLS_SRC.glob("kv-*") if p.is_dir())
for skill_dir in skill_dirs:
    copy_skill_tree(skill_dir, GROK_SKILLS)
    copy_skill_tree(skill_dir, PKG / "skills")

count = len(list((PKG / "skills").glob("kv-*/SKILL.md")))
print(f"Synced skills/kv-* -> {GROK_SKILLS}")
print(f"Synced skills/kv-* -> {PKG / 'skills'}")
print(f"Synced AGENTS.md, Bootstrap.md -> {PKG}")
print(f"Package MEMORY + DailyChange -> blank seeds (not vault private data)")
print(f"skills/kv-* packages: {count}")
