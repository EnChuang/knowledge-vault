---
name: kv-token
description: >
  Knowledge Vault token budget and output discipline. Use for long Source reads,
  full-library grep, multi-file writes, or when context is large. Cold-start
  reads only AGENTS + triggered skills, not full Canon unless required.
metadata:
  short-description: "KV token budget — cold start, read discipline"
---

# kv-token — 讀取預算與產出分流

## 與 Grok_rules §0

本 Skill 與 `AGENTS.md`「依任務載入 Skill」為**讀取節制**準則。`Grok_rules` §0「幾乎必讀」適用**健檢、改規則、更名**等須對照 Canon 全文的任務；一般討論／草稿若當次 Skill 摘要夠用，**不預載四 L1 全文**。

衝突時：**用戶指令 ＞ 當次 Skill ＞ 本 Skill ＞ Grok_rules §0 摘要**。

## 冷啟動（預設）

| 載入 | 不載入 |
|------|--------|
| `AGENTS.md`（常駐） | `Bootstrap.md`（除非 kv-bootstrap） |
| 當次 **kv-* Skill** | 四 L1 Canon 全文（除非 Skill 明確要求） |
| 任務相關 `Project/` 筆記 | 全庫逐篇掃描 |

## 讀取節制

- **先 Skill、後 Canon**：Skill 摘要夠用則不讀 Canon
- **先規則、後筆記**：依 AGENTS 資料搜尋階層
- **止搜**：夠支撐當次討論／寫入即可
- **例外**：更名／健檢 → 須全庫 grep（kv-rename、kv-audit）
- **引讀例外**：指定 Source 須讀完（kv-source），不外擴全庫

## 產出分流

| 類型 | 去向 | 聊天室 |
|------|------|--------|
| 對抗審查 L-全 | `Project/_DailyChange/DailyChange.md` 當期區 | 僅 Verdict 摘要；勿讀淘汰摘要全文 |
| 跨 Session 脈絡 | `MEMORY.md` | 按需讀；勿當 transcript |
| 整理筆記草稿 | 待用戶請寫入 | 可貼草稿或摘要 |
| 健檢報告 | 聊天（未請寫入） | G1–G10 表格式 |
| 規則討論 | 草稿 | 不貼 Canon 全文 |

## Project 筆記

- **維持白皮書敘事**；不將 Project 正文 caveman 化
- 規則執行層可精簡；產出層保持可讀段落

## 長任務

- 分段蒸餾（kv-source §4）優於一次傾倒
- 大規模 grep 結果：待改清單表格式，不逐檔貼全文