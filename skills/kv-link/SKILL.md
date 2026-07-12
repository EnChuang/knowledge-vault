---
name: kv-link
description: >
  Knowledge Vault wikilinks — Source piped links vs knowledge nodes, high-frequency
  nodes, vocabulary. Use when writing content with links or after renames.
metadata:
  short-description: "KV wikilinks — Source vs nodes"
---

# kv-link — 內部連結

Canon：`Grok_rules.md` §5。

## 兩類型（不可混用）

| 類型 | 寫法 |
|------|------|
| **Source** | `[[Source/…/檔.副檔名\|顯示名]]` |
| **知識節點** | `[[節點名稱]]` |

知識節點不帶路徑；卡片未建仍可寫 wikilink；不主動建佔位 `.md`。

## 高頻節點（正文必須 wikilink）

`[[Agent Harness]]` · `[[Session]]` · `[[MOC]]` · `[[Grok Build]]`

## 建立順序

依 AGENTS 資料搜尋階層掌握脈絡 → 優先同專題節點 → 再跨專題。

## 批次掃描

全庫／專題**未連結節點**掃描與請寫入套用 → **kv-link-scan**（預設只報告）。

## 用詞

知識庫 · 庫根目錄 · 全庫 · 本實例 → 見 `AGENTS.md`。