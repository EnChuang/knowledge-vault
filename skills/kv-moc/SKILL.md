---
name: kv-moc
description: >
  Knowledge Vault MOC format — four sections, nested wikilink tree, M1–M10 checks.
  Use when reading/writing {專題} — MOC.md or syncing MOC after writing sub-notes.
metadata:
  short-description: "KV MOC — four sections, M1–M10"
---

# kv-moc — 專題 MOC

Canon：`MOC_rules.md`。每專題必須 `Project/{專題}/{專題名稱} — MOC.md`。

## §2 固定結構（順序不可改）

```markdown
# {專題名稱} — MOC
## 專題簡介
## 筆記關係樹狀圖
## 文獻來源
## 待延伸
```

frontmatter：`title`（＝檔名）、`type: moc`、`tags`（專題 + `方法論/MOC`）、`created`、`updated`。

## §3 各章節

| 章節 | 規範 |
|------|------|
| 簡介 | 2–5 句；禁貼全文 |
| 樹 | 巢狀 `[[wikilink]]`；**禁 mermaid**；只鏈**已存在**筆記；根層專題名粗體 |
| 文獻 | 專題 Source 元索引；piped link 含副檔名 |
| 待延伸 | 新建留空；延伸+請寫入後才 `- [ ]` |

`（待建立）` 僅延伸+請寫入後（§8）。

## §4 M1–M10

M1 僅請寫入子筆記觸發 · M2 四段順序 · M3 巢狀 wikilink · M4 不預填 · M5 簡介2–5句 · M6 樹名＝檔名 · M7 文獻格式 · M8 元索引 · M9 命名 · M10 標籤無空格

## §5 維護

請寫入子筆記 → 同步簡介+樹；更名 → kv-rename；僅討論 → 不動 MOC；新建專題 → 最小四段空架。

同專題新 Source 致地圖不均、需拆併重劃 → **kv-rebalance**（Canon：`MOC_rules` §7）。

## §6 生長

不預設地圖；禁止討論中途預填規劃子題。

## §8 待延伸

配合 kv-flow §8：討論中不新增；同意+請寫入才可加。