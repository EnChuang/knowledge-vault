---
name: kv-rules-sync
description: Use when changing Knowledge Vault rules, AGENTS.md, Bootstrap.md, or kv-* skills, including synchronization to runtime and open-box copies.
metadata:
  short-description: "KV rules sync — L0/L1/Skill/seed"
---

# kv-rules-sync — 規則同步

## Overview

L0／L1／Skill／Bootstrap 交叉同步與開箱對齊。  
改規則後必跑。
方針：全庫統一的只有定位（Overview）＋少數硬閘／步驟方向；其餘表述、舉例、臨場策略不制式化，容許容錯與自由發揮。設計型若要鎖風格，再個別補 Reference，不上升成全庫義務。

## Agent 使用步驟

1. 對照落差（AGENTS、Canon、Skill、Bootstrap）。
2. 請寫入後改種子／索引；必要時 sync_package。
3. 開箱包勿帶入個資 MEMORY／DailyChange 正文。

## 原則

規範定案 → 寫 **Canon**（對應 `*_rules.md`）+ 同步 **Skill** + **`Bootstrap.md` 種子** + **`AGENTS.md` 索引**（若職責變）。

日常真相：磁碟 Canon + `skills/`。Bootstrap 種子為重置快照。

## L0/L1 對照（新增／更名必跑）

| 觸發 | L0 必查 | 全部必查 |
|------|---------|----------|
| 新增條文 | AGENTS 任務表、Skill 表 | 目標 Canon；grep 其餘 L1+skills |
| 新建 L1 | 啟動前置、分類軸 | 讀四 Canon + 查 Skill 重複 |
| 更名 | AGENTS、Bootstrap、For Reader | grep 舊名於 L0+四L1+skills |
| 架構定案 | — | 同步 `建庫開箱（打包用）/`（G9） |

## 寫入規則檢查（kv-flow §3 D）

D1 層級（L0 只索引）· D2 歸檔 · D3 落差清單 · D4 AGENTS · D5 Bootstrap 種子 · D6 grep 四L1+L0+skills

## 寫入後（§4 C）

C1 落差回報 · C2 未擅自改歷史筆記 · C3 交叉引用 · C4 Bootstrap · C5 L0/L1 對照

## 健檢級別

- **小改**：grep L0+四L1+skills；更新對應 Bootstrap 種子
- **結構改**：讀全部 Canon+AGENTS+skills；更新任務表與開箱包

## Skill 鏡像同步（改 `skills/` 或 L0 涉架構後必跑）

磁碟真相源：`skills/kv-*/`（打包用母本）。**不會**自動複製；須執行：

```bash
python skills/kv-link-scan/scripts/sync_package.py
```

| 目標 | 用途 |
|------|------|
| `~/.codex/skills/` | Codex 個人全域 Skill（**主要執行**） |
| `.agent/skills/` | 其他執行載具的相容鏡像 |
| `建庫開箱（打包用）/建庫開箱（打包用）/` | G9 開箱包（AGENTS、Bootstrap、skills、Review 種子） |

只同步 `kv-*`；不得覆寫 `~/.codex/skills/.system/` 或其他個人 Skill。

改 Canon 且 Skill 摘要需對齊 → 先改 `skills/kv-*/SKILL.md`，再跑上列腳本。打包前另跑 **kv-audit** G9。

