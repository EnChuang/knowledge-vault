---
name: kv-flow
description: Use when the user explicitly asks to write, save, rename, repair, or otherwise persist changes in the Knowledge Vault. Do not use to mutate files during discussion-only requests.
metadata:
  short-description: "KV write flow — §3/§4 checks, discussion extension"
---

# kv-flow — 寫入流程與檢查

Canon 全文：`Workflow_rules.md` §2–§4、§8。執行以本 Skill 為準。

## Overview

寫入閘與 §3／§4 檢查：未請寫入只草稿。  
Canon：`Workflow_rules.md` §2–§4、§8。方針：全庫統一的只有定位（Overview）＋少數硬閘／步驟方向；其餘表述、舉例、臨場策略不制式化，容許容錯與自由發揮。設計型若要鎖風格，再個別補 Reference，不上升成全庫義務。

## Agent 使用步驟

1. 判定是否請寫入；否則只草稿／討論。
2. 請寫入 → kv-method L-全 → §3 全過 → 寫入 → §4 → 簡報。
3. 更名／健檢修復走對應分支（E／F）。

## §1 核心（摘要）

| 原則 | 行為 |
|------|------|
| 寫入 | 未說「請寫入」等 → **只草稿** |
| 語言 | 中文 → 繁體中文；**中文術語完整**（禁英譯半截詞，見 Project_rules） |
| 證據 | 禁止自行發明數據 |
| 規則歸屬 | 規範只寫 L0/Skill/Canon |
| 連結 | **kv-link**；每句 ≤2–3 wikilink |
| 講解重點 | 整理／蒸餾時 **kv-project**：**科普掃讀**＋卡點一句譬喻；非 Ebook 須 30 秒帶走／收束 |

## §2 流程

```
內容/Source
  →（引用）kv-source 引讀五步 → kv-project 覆蓋複核（一般筆記自測／指南 FAQ）
  →（討論）蒸餾 → 覆蓋複核 → 草稿
  → 用戶「請寫入」
  → kv-method L-全（Blocked 則停）
  → §3 全過 → 寫入 → §4 → 簡報
  → §8 告一段落才問延伸

更名 → kv-rename → 請寫入 → §3 E → §4 E
健檢修復 → kv-audit 報告 → 請寫入 → §3 F → §4 F
```

## §3 寫入前（請寫入後、改檔前）

### A 通用

| # | 通過條件 |
|---|----------|
| A1 | 僅指定檔／段（kv-project §8） |
| A2 | Source 帶路徑+副檔名；知識節點無路徑 |
| A3 | 高頻節點 wikilink 統一 |
| A4 | 圖在 `Source/Image/` |
| A5 | 非 Ebook：科普掃讀（30 秒／分鏡／收束）；Ebook §12 另遵（§2 例外可冷寫） |
| A6 | 無自動討論問題、無預填 MOC |

### B Project

B1 MOC 連動 · B2 只加本次筆記 · B3 frontmatter+tags · B4 非規則條文 · B5 80%自足＋命題可復述 · B6 三一致命名 · B7 一般筆記自測或使用指南 FAQ／操作覆蓋複核通過 · B8 非 Ebook：有 30 秒與收束、禁長散文牆

### C Source

C1 頁碼範圍 · C2 事實對齊 · C3 piped link · C4 引讀完成

### D 規則檔

D1 層級 · D2 歸檔 · D3 落差清單 · D4 AGENTS 索引 · D5 Bootstrap 種子 · D6 L0/L1 grep

### E 更名

E1 全庫清單 · E2 三一致 · E3 MOC 連動

### F 健檢修復

F1 僅待修項 · F2 G9 開箱包

## §4 寫入後

A 可讀/連結/簡報 · B MOC 已更新/格式/標籤 · C 落差/Bootstrap/L0對照 · D 失敗說明 · E 更名殘留複查 · F 健檢複查+G9

## §8 討論延伸

討論中禁止自動塞問題；結束才問；同意+請寫入才可寫 MOC「待延伸」。

## 工具能力（依 Harness 對應）

| 用途 | 工具 |
|------|------|
| 讀 Canon／Project／Source | 檔案讀取工具 |
| 全庫對照、連結、命名殘留 | 優先 `rg`／檔案搜尋 |
| 請寫入改檔 | Codex 使用 `apply_patch`；其他 Harness 使用其安全編輯工具 |
| 腳本（kv-link-scan、sync_package） | 終端機命令；Windows 優先 PowerShell |

