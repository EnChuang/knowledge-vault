---
name: kv-rename
description: >
  Knowledge Vault rename and move — full-library grep, update paths, MOC, tags,
  L0/L1, 建庫開箱. Use when renaming topics, notes, Source files, or significant
  note revisions requiring tag alignment.
metadata:
  short-description: "KV rename — full-library grep §10"
---

# kv-rename — 更名與搬移

Canon：`Project_rules.md` §10。不受日常搜尋節制限制。

## 觸發

專題資料夾 · 專題索引 · 子筆記更名 · Source 路徑變更 · 顯著改版（對齊 tags）

## 原則

1. 舊名→新名對照表
2. **全庫 grep** 舊名 → 待改清單
3. 用戶確認範圍
4. 用戶「請寫入」→ kv-flow §3 E → 搬移更新
5. 再 grep 殘留
6. kv-flow §4 E 簡報

## 全庫清單（至少）

| # | 檢查處 |
|---|--------|
| 1 | 實體路徑（Project、Source） |
| 2 | frontmatter：`title`、`parent`、**`tags`**、`updated` |
| 3 | 同專題 MOC（檔名、樹、簡介、tags） |
| 4 | 專題索引頁 |
| 5 | Project 正文 wikilink |
| 6 | 跨專題 MOC／筆記 |
| 7 | L0、`AGENTS.md`、`Bootstrap.md`、四 L1、`skills/` |
| 8 | Source piped link 全文路徑 |
| 9 | `建庫開箱（打包用）/` |

三一致：檔名＝`title`＝wikilink。MOC 連動 → kv-moc §5。