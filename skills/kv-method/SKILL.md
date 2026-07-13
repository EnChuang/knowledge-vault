---
name: kv-method
description: >
  Knowledge Vault first-principles and adversarial review (L-light / L-full).
  Use for every task (L-light). Use L-full before deliverables, 請寫入, rule changes,
  renames, or full-library audit. Writes review log to Project/_DailyChange/, not chat.
when-to-use: >
  Every task (L-light). L-full on 請寫入, 存入, 建立卡片, deliverables, rule or Skill
  changes, renames, audit repair, or 建庫開箱 sync.
allowed-tools: Read, Grep, Glob, Write, StrReplace
metadata:
  short-description: "KV methodology — first principles + adversarial review"
---

# kv-method — 第一性原理與對抗審查

> **人類用語**：**L-輕**＝輕量審查（討論、草稿）；**L-全**＝完整交付審查（請寫入、改規則、更名、健檢）；日誌寫 [[DailyChange]]。

讀取後依本 Skill 執行；細節 Canon 見 `Grok_rules` §1–§2（方法論擴充）。

## 第一性原理（每任務）

動手前先簡答（L-輕可內心完成，L-全須寫入日誌）：

1. **根本問題**：用戶真正要解決什麼？成功長怎樣？
2. **可驗證拆解**：假設與依賴是什麼？如何證偽？
3. **決策 why**：為何選此做法而非替代方案？

## 分級

| 級別 | 時機 | 行為 |
|------|------|------|
| **L-輕** | 一般討論、草稿、探索 | 三步簡答；回覆不貼審查全文 |
| **L-全** | 請寫入、交付、改規則、更名、健檢修復、架構變更 | 完整 12 節對抗審查 → 寫日誌 → Fatal 則阻塞交付 |

## L-全 觸發（任一即 L-全）

- 用戶「請寫入」「存入」「建立卡片」
- 修改 L0/L1/Skill/Bootstrap
- 全庫健檢報告後修復
- 更名／搬移執行
- 打包 `建庫開箱（打包用）/`

## L-全 流程

1. 完成 **kv-project** 讀者自測（若涉整理筆記）或等價驗證
2. 跑 12 節對抗審查（模板 → `references/adversarial-review.md`）
3. 寫入 **`Project/_DailyChange/DailyChange.md`**（見 §日誌輪替）
4. **Final Verdict**：Pass / Pass-with-Notes / **Blocked**
5. 回覆用戶：僅摘要（Verdict + Fatal 數 + 日誌路徑）；**勿貼 12 節全文**
6. **Blocked**（Fatal Problems）→ 不得請寫入／交付，先修復再 L-全

## §日誌輪替（`_DailyChange` 僅一檔）

| 規則 | 說明 |
|------|------|
| **唯一檔名** | `Project/_DailyChange/DailyChange.md`；禁止再建日期前綴多檔 |
| **覆寫當期** | 新 L-全 前：將舊「當期」壓成「淘汰摘要」表一行（日期／任務／Verdict／理由） |
| **開放風險** | 跨任務仍有效之項留表；已關閉則刪列 |
| **淘汰摘要上限** | 最多 **15 行**；超過刪最舊行 |

### AI 淘汰判定（寫入新當期前執行）

| **刪／不保留全文** | **保留** |
|-------------------|----------|
| 已交付且結論已進 `Project/` 筆記或 L0/L1 | 當期完整 12 節（至下次 L-全） |
| 健檢／修復已關閉的待修項 | **Blocked** 未解的 Fatal |
| Token-Bench、一次性實驗資料 | 開放風險表中仍有效項 |
| 規劃／自審全文（權威在總編／正文） | 淘汰摘要每任務一行 |

**禁止**為歷史任務另建 `_DailyChange/*.md`。跨 Session 交班 → 庫根 **`MEMORY.md`**（**kv-memory**）；研究正文 → `Project/` 筆記。

## 12 節標題（L-全 日誌必含）

1. Task Restatement · 2. Success Criteria · 3. First-Principles Decomposition · 4. Assumptions & Dependencies · 5. Plan vs Alternatives · 6. Rule/Skill Compliance · 7. Evidence & Canon Alignment · 8. Edge Cases · 9. Token/Scope Discipline · 10. Pre-Mortem · 11. Residual Risks · 12. Final Verdict（含 Fatal Problems）

涉知識長文時：§6 或 §11 附 **Narrative Quality**（鉤子／命題／收束／卡點譬喻／表開場）。通篇條列無敘事 → Fatal；譬喻偏少 → Pass-with-Notes。

## 與其他 Skill

- 寫入檢查仍走 **kv-flow** §3/§4
- L-全 不取代讀者自測；自測通過後才跑 L-全
- 請寫入交付成功後 → **kv-memory** 視需要更新 `MEMORY.md`（與變更日誌分開）