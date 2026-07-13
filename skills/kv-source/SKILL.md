---
name: kv-source
description: >
  Knowledge Vault Source handling — literature/Ebook/Image links, Ebook page checks,
  five-step Source 引讀, Ebook default chapter format (Project_rules §12).
  Use when citing PDFs, ebooks, images, or user points to Source/ files.
metadata:
  short-description: "KV Source — 引讀五步, Ebook §12, images"
---

# kv-source — Source 與引讀

Canon：`Source_rules.md`。原文不存在 → 告知用戶，不發明。

## §1 子資料夾

`Source/literature/` · `Source/Ebook/` · `Source/Image/` — 不按專題分夾。

## §2 連結

- 文獻：`[[Source/literature/檔.pdf|名]]`
- 圖：`![[Source/Image/檔.jpg|寬]]`
- 必含副檔名；禁為實體檔建同名 `.md`
- 新圖存 `Source/Image/`
- 更名 → kv-rename 更新 piped link

## §3 Ebook

- 未引用：禁整本掃描
- 引用：走 §4 引讀
- 非引讀：定位→核對→確認→整理（用戶可說不用核對）

## §4 引讀五步（不可跳步）

| 步 | 行為 |
|----|------|
| 1 讀完 | 用戶所指範圍全部內容 |
| 2 大綱 | 依來源自身結構 |
| 3 對齊 | 與用戶確認大綱 |
| 4 蒸餾 | 分段討論，慢慢蒸餾 |
| 5 自測 | kv-project §3；Ebook 加 §12 閘門與答案寫入 |

引讀指定 Source 時，搜尋節制不適用於該來源（須讀完，不外擴全庫）。

影片／文獻／電子書皆適用；無法取得全片須說明限制。

同專題已有筆記又來新 Source（新子域／舊卡過肥）→ **kv-rebalance**，勿預設只 append 舊卡。

## §5 Ebook 蒸餾預設

Canon：`Source_rules.md` §5、`Project_rules.md` §12。

| 預設 | 內容 |
|------|------|
| 觸發 | `Source/Ebook/` 引讀蒸餾，用戶**未**另指定格式 |
| 專題 | 一書一專題＋MOC 對齊章節 |
| 單章 | kv-project §12 骨架（公式＋註解＋比喻、10 題、答案區、Exam 閘門） |
| 例外 | 用戶明確要求其他文風 → 以用戶指令為準 |

步 4 按章產草稿；步 5 通過 10/10 且答案寫入後，用戶「請寫入」定稿。