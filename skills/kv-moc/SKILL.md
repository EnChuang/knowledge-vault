---
name: kv-moc
description: Use when reading, creating, editing, or validating a Knowledge Vault topic MOC, or synchronizing its tree after topic-note changes.
metadata:
  short-description: "KV MOC — five sections, 整理規範, M1–M10"
---

# kv-moc — 專題 MOC

Canon：`MOC_rules.md`。每專題必須 `Project/{專題}/{專題名稱} — MOC.md`。

## Overview

MOC 五段格式與 M1–M10 檢查。  
Canon：`MOC_rules.md`。
方針：全庫統一的只有定位（Overview）＋少數硬閘／步驟方向；其餘表述、舉例、臨場策略不制式化，容許容錯與自由發揮。設計型若要鎖風格，再個別補 Reference，不上升成全庫義務。

## Agent 使用步驟

1. 讀／寫 `{專題} — MOC.md` 時對齊五段。
2. 子筆記寫入後同步樹與規範。
3. 跑 M1–M10；缺則補或標待確認。

## §2 固定結構（順序不可改）

```markdown
# {專題名稱} — MOC
## 專題簡介
## 整理規範
## 筆記關係樹狀圖
## 文獻來源
## 待延伸
```

frontmatter：`title`（＝檔名）、`type: moc`、`tags`（專題 + `方法論/MOC`）、`created`、`updated`。

## §3 各章節

| 章節 | 規範 |
|------|------|
| 簡介 | 2–5 句；禁貼全文；邊界／是什麼 |
| **整理規範** | **本專題**怎麼蒸餾／寫筆記（列點 vs 敘事、故事比重等）；可空架；長規另檔 + wikilink；**非** L0/L1 |
| 樹 | 巢狀 `[[wikilink]]`；**禁 mermaid**；只鏈**已存在**筆記；根層專題名粗體 |
| 文獻 | 專題 Source 元索引；piped link 含副檔名 |
| 待延伸 | 新建留空；延伸+請寫入後才 `- [ ]` |

`（待建立）` 僅延伸+請寫入後（§8）。

寫入子筆記前：讀本專題「整理規範」；已定案則對齊體裁（可覆蓋全庫科普掃讀預設之**定向**，不可放寬寫入閘門）。

## §4 M1–M10

M1 僅請寫入觸發 · M2 **五段**順序 · M3 巢狀 wikilink · M4 不預填（整理規範可空） · M5 簡介2–5句 · M6 樹名＝檔名 · M7 文獻格式 · M8 元索引 · M9 命名 · M10 標籤無空格

## §5 維護

請寫入子筆記 → 同步簡介+樹；整理規範僅用戶改約定時更新；更名 → kv-rename；僅討論 → 不動 MOC；新建專題 → 最小**五段**空架。

同專題新 Source 致地圖不均、需拆併重劃 → **kv-rebalance**（Canon：`MOC_rules` §7）。

## §6 生長

不預設地圖；禁止討論中途預填規劃子題。

## §8 待延伸

配合 kv-flow §8：討論中不新增；同意+請寫入才可加。
