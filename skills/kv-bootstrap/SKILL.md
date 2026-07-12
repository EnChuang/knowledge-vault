---
name: kv-bootstrap
description: >
  Knowledge Vault bootstrap B0–B7 — build empty vault from AGENTS.md + Bootstrap.md seeds.
  Use when only AGENTS.md exists, L1 files missing, or user resets rule system.
metadata:
  short-description: "KV bootstrap — B0–B7 build empty vault"
---

# kv-bootstrap — 建庫開箱

讀 `Bootstrap.md` 全文。空庫僅有 `AGENTS.md` 時執行。

## B0 順序

1. B1 目錄骨架（含 `MEMORY.md`、`Project/_DailyChange/DailyChange.md`、`skills/`）
2. 確認 `AGENTS.md` + `Bootstrap.md`
3. 複製 `skills/kv-*/` → 庫根 `.grok/skills/`（**必須**；每 skill 一資料夾含 `SKILL.md`）。**勿**覆寫 `~/.grok/skills/` 內建 Skill
4. B3–B6 依序建 Canon：`Grok_rules` → `MOC_rules` → `Project_rules` → `Source_rules`
   - 種子為 MRC 摘要；**須從開箱包或完整庫複製詳盡 Canon**（若本庫為完整實例則複製庫根四 L1）
5. B7 驗收回報
6. 列出最終檔案樹

## 勿跳步

Grok Canon 先建（§3–§4 引用其他 L1），其餘三檔次依序，再跑 B7。

## 驗收 V1–V7

見 `Bootstrap.md` B7。未過 → 修正後更新種子版本號。

## 與 Skill 體系

建庫後日常執行靠 **AGENTS + kv-***，不常駐載入 Bootstrap 或四 L1 全文。