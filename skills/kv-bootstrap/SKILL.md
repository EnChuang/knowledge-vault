---
name: kv-bootstrap
description: Use when a Knowledge Vault is empty, any required L1 rule file is missing, only AGENTS.md remains, or the user explicitly requests a rule-system reset.
metadata:
  short-description: "KV bootstrap — B0–B7 build empty vault"
---

# kv-bootstrap — 建庫開箱

## Overview

空庫／重置：依 Bootstrap.md B0→B7 重建規則體系。  
種子權威在 `Bootstrap.md`。
方針：全庫統一的只有定位（Overview）＋少數硬閘／步驟方向；其餘表述、舉例、臨場策略不制式化，容許容錯與自由發揮。設計型若要鎖風格，再個別補 Reference，不上升成全庫義務。

## Agent 使用步驟

1. 確認為空庫或用戶要重置。
2. 依 B0→B7 建立／還原 L1、目錄、種子。
3. 完成後回到 AGENTS 啟動前置檢查。

讀 `Bootstrap.md` 全文。空庫僅有 `AGENTS.md` 時執行。

## B0 順序

1. B1 目錄骨架（含 `MEMORY.md`、`Project/_DailyChange/DailyChange.md`、`skills/`）
2. 確認 `AGENTS.md` + `Bootstrap.md`
3. 複製 `skills/kv-*/` → 個人 Skill 目錄（主要）及庫根 `.agent/skills/`（相容鏡像）；每個 Skill 一資料夾且含 `SKILL.md`。只同步 `kv-*`，勿覆寫系統或其他個人 Skill
4. B3–B6 依序建 Canon：`Workflow_rules` → `MOC_rules` → `Project_rules` → `Source_rules`
   - 種子為 MRC 摘要；**須從開箱包或完整庫複製詳盡 Canon**（若本庫為完整實例則複製庫根四 L1）
5. B7 驗收回報
6. 列出最終檔案樹

## 勿跳步

Workflow Canon 先建（§3–§4 引用其他 L1），其餘三檔次依序，再跑 B7。

## 驗收 V1–V7

見 `Bootstrap.md` B7。未過 → 修正後更新種子版本號。

## 與 Skill 體系

建庫後日常執行靠 **AGENTS + kv-***，不常駐載入 Bootstrap 或四 L1 全文。


