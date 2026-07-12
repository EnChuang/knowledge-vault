# 對抗審查日誌模板（完整交付審查／Skill 內碼 L-全）

**唯一路徑**：`Project/_DailyChange/DailyChange.md`（覆寫「當期」區；舊任務一行入「淘汰摘要」。見 kv-method §日誌輪替。）

```markdown
---
title: DailyChange
tags:
  - 方法論/DailyChange
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
---

# DailyChange

> **當期變更日誌**（人類可讀）。本夾僅此一檔；每次**完整交付審查**後覆寫「當期」區。Session 交班（僅 AI）→ 庫根 `MEMORY.md`。

---

## 當期（最新一輪完整交付審查）

**任務**：{任務簡稱}

### 1. Task Restatement
### 2. Success Criteria
### 3. First-Principles Decomposition
### 4. Assumptions & Dependencies
### 5. Plan vs Alternatives
### 6. Rule/Skill Compliance
### 7. Evidence & Canon Alignment
### 8. Edge Cases
### 9. Token/Scope Discipline
### 10. Pre-Mortem
### 11. Residual Risks

### 12. Final Verdict

| 項目 | 內容 |
|------|------|
| **Verdict** | Pass / Pass-with-Notes / Blocked |
| **Fatal Problems** | （無則寫「無」） |
| **Notes** | 非阻塞建議 |

---

## 開放風險（跨任務，仍有效才留）

| 項 | 來源 | 狀態 |

---

## 淘汰摘要（每任務一行，滿 15 行刪最舊）

| 日期 | 任務 | Verdict | 淘汰理由 |
```

寫入前：讀取現有檔 → 當期區壓一行進淘汰摘要 → 更新開放風險 → 覆寫當期。