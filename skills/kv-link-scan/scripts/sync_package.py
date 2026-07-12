#!/usr/bin/env python3
"""Sync library root AGENTS, Bootstrap, skills/kv-* to .grok/skills/ and 建庫開箱（打包用）."""
from __future__ import annotations

import shutil
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
PKG = VAULT / "建庫開箱（打包用）" / "建庫開箱（打包用）"
GROK_SKILLS = VAULT / ".grok" / "skills"
SKILLS_SRC = VAULT / "skills"


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


for name in ("AGENTS.md", "Bootstrap.md", "MEMORY.md"):
    src = VAULT / name
    if src.exists():
        shutil.copy2(src, PKG / name)

review_seed = VAULT / "Project" / "_DailyChange" / "DailyChange.md"
if review_seed.exists():
    out_review = PKG / "Project" / "_DailyChange" / "DailyChange.md"
    out_review.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(review_seed, out_review)

skill_dirs = sorted(p for p in SKILLS_SRC.glob("kv-*") if p.is_dir())
for skill_dir in skill_dirs:
    copy_skill_tree(skill_dir, GROK_SKILLS)
    copy_skill_tree(skill_dir, PKG / "skills")

count = len(list((PKG / "skills").glob("kv-*/SKILL.md")))
print(f"Synced skills/kv-* -> {GROK_SKILLS}")
print(f"Synced skills/kv-* -> {PKG / 'skills'}")
print(f"Synced AGENTS.md, Bootstrap.md, MEMORY.md -> {PKG}")
print(f"skills/kv-* packages: {count}")