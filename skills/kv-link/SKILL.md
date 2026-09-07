---
name: kv-link
description: Use when writing or repairing Knowledge Vault wikilinks, distinguishing Source file links from knowledge-node links, or aligning links after a rename.
metadata:
  short-description: "KV wikilinks — Source vs nodes"
---

# kv-link — 內部連結

Canon：`Workflow_rules.md` §5。

## Overview

wikilink 兩類型（Source piped vs 知識節點）與高頻節點。  
Canon：`Workflow_rules.md` §5。**規則型**。批次維護另載 **kv-link-scan**。

## Agent 使用步驟
方針：全庫統一的只有定位（Overview）＋少數硬閘／步驟方向；其餘表述、舉例、臨場策略不制式化，容許容錯與自由發揮。設計型若要鎖風格，再個別補 Reference，不上升成全庫義務。


1. 寫入含連結時區分 Source／知識節點寫法。
2. 高頻節點必須 wikilink；優先同專題。
3. 掃描／修剪需求 → 轉 kv-link-scan。

## 兩類型（不可混用）

| 類型 | 寫法 |
|------|------|
| **Source** | `[[Source/…/檔.副檔名\|顯示名]]` |
| **知識節點** | `[[節點名稱]]` |

知識節點不帶路徑；卡片未建仍可寫 wikilink；不主動建佔位 `.md`。

## 高頻節點（正文必須 wikilink）

`[[AI Agent 工程]]` · `[[MEMORY]]` · `[[DailyChange]]` · `[[Architecture-Status]]`

## 建立順序

依 AGENTS 資料搜尋階層掌握脈絡 → 優先同專題節點 → 再跨專題。

## 批次掃描

全庫／專題超連結維護（未連結補上、弱／過密修剪、圖改 Source 路徑）→ **kv-link-scan**（預設只報告；請寫入才改檔）。

## 用詞

知識庫 · 庫根目錄 · 全庫 · 本實例 → 見 `AGENTS.md`。

