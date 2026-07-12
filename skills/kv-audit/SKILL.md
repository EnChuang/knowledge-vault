---
name: kv-audit
description: >
  Knowledge Vault full-library alignment audit G1–G10. Use for 全庫健檢, 對齊檢查,
  打包前檢查, or after large renames. Report only unless user says 請寫入; G9 required
  before copying 建庫開箱（打包用）.
metadata:
  short-description: "KV audit — G1–G10 full-library check"
---
# kv-audit — 全庫對齊健檢

Canon：`Grok_rules.md` §9。未請寫入 → 只出報告。

## 觸發

用戶明確要求 · 大規模更名後建議 · **打包開箱包前必跑**

## G1–G10

| G#  | 領域          | 通過條件                                      |
| --- | ------------- | --------------------------------------------- |
| G1  | 命名殘留      | grep 舊名、含空格舊 tags；無未處理殘留        |
| G2  | 知識 wikilink | `Project/`、L0/L1 內 `[[節點]]` 目標存在  |
| G3  | Source 連結   | piped link、圖片路徑實體存在                  |
| G4  | 圖片          | 孤兒圖列出；**用戶確認後**才刪          |
| G5  | MOC           | 四段齊；M1–M10；樹只鏈存在筆記               |
| G6  | frontmatter   | 三一致；tags 無空格                           |
| G7  | 目錄          | Project/README 與實體一致                     |
| G8  | L0/L1/Skill   | AGENTS、Canon、Bootstrap、skills 無非刻意漂移 |
| G9  | 開箱包        | `建庫開箱（打包用）/` 與庫根對齊            |
| G10 | 規則歸屬      | Project 筆記內無 AI 規則條文                  |

## 產出

報告含 G1–G10（通過／待修／刻意保留）、待修清單（路徑+動作）。

修復 → kv-flow §3 F → §4 F；涉架構同步開箱包 + kv-rules-sync。
