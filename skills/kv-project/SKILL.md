---
name: kv-project
description: >
  Knowledge Vault Project notes — whitepaper style, reader self-test (10–20 Q),
  Ebook chapter template (formula+annotation+metaphor, exam gate, answer section),
  tags without spaces, naming, narrative rhythm. Use analogy when explaining or
  organizing note highlights. Use for subtopic discussion, distillation, Ebook
  chapter notes, or writing Project/ notes.
when-to-use: >
  整理筆記、蒸餾重點、子主題討論、電子書章節筆記、講解筆記重點、白皮書草稿；
  須用比喻釐清抽象概念。Source/Ebook/ 引讀預設 §12 格式。
metadata:
  short-description: "KV Project — whitepaper, Ebook §12, self-test, tags"
---

# kv-project — Project 筆記

Canon：`Project_rules.md`。前置：AGENTS 啟動前置；寫入前須有 MOC（或同次建最小 MOC）。**例外**：`配色查詢表.md` → **kv-palette**（§13，免 MOC／自測）。

## §2 白皮書

讀者**只讀此檔**應掌握當次核心約 **80%**。

| 目標 | 要求 |
|------|------|
| 自足 | 跨篇連結僅開頭銜接／結尾延伸 |
| 可掃讀 | 章節骨架，非聊天紀錄 |
| 去噪 | 無導流、無關副案例 |

骨架：定位 → 問題 → 概念 → 結構 → 實踐 → 結論 → 延伸閱讀。

## §3 讀者自測（請寫入前必跑）

1. 出 **10–20 題**（紧扣核心；不問推廣）；**Ebook §12** → 每章 **10 題**
2. **讀者**僅讀正文作答（不查 Session/Source/他篇）
3. 答不出 → 補正文 → 重測；Ebook → **10/10 閘門**
4. 有 Source 引讀時為引讀第 5 步
5. 寫入後簡報題數與通過項；Ebook → **答案區寫入筆記**（§12 版型）

## §4 命名

檔名＝`title`＝wikilink。禁 `討論`、`草稿`、`untitled`、純日期。宏觀可用 `… 概論`。

Ebook 章節：`{章號} · {章標題}.md`。

## §5–§7 文風

- 介紹期段落敘事；進入原理後才列表／表
- 禁止通篇條列、正文中途跨筆記引用
- 跨篇連接只放開頭或結尾延伸

## §5b 比喻釐清（講解整理重點時必用）

Canon：`Project_rules.md` §5「講解整理重點：比喻釐清」。

| 時機 | 行為 |
|------|------|
| 向用戶講解／整理重點（草稿或正文） | **至少一則**貼切比喻 + 一句原理收斂 |
| 艱澀概念、層級、取捨 | 比喻開路；可接簡表對照 |
| 聊天室草稿 | 重點段落含比喻，不只條列 |

先喻後理；一重點一主比喻；不取代精確定義。

## §8 分段

未請寫入 → 只出該段草稿；請寫入 → 只替換指定段。

## §9 標籤

- 格式 `領域/子領域`；**禁止空格**
- 多詞用連字號：`AI/Harness`、`方法論/Loop-Engineering`
- ❌ `AI/Agent Harness`
- 更名／顯著改版同步 `tags` + `updated`
- MOC：第一 tag 專題歸屬；第二 `方法論/MOC`
- Ebook 章節：第二 tag 可用 `{領域}/Handbook`

## §10–§11

更名全庫對照 → **kv-rename**。健檢 → **kv-audit** G1/G5/G6/G7。

## §12 Ebook 蒸餾（預設）

Canon：`Project_rules.md` §12。**`Source/Ebook/` 引讀且用戶未另指定格式時必用。**

### 單章順序

銜接／出處 → `本章只記這幾件事`（≤5）→ `公式與註解`（`$$`＋符號表＋比喻）→ `實務一句` → `讀者自測（10 題）` → `讀者自測答案` → `<!-- Exam: 10/10 pass -->`

### 文風

公式優先；快懂；**預設不嵌圖**；正文不穿插「見 Ch.x」。

### 答案版型

```markdown
## 讀者自測答案

> 建議先遮住本區、對照上方題目自答，再逐題核對。**粗體**＝必記要點；*斜體*＝直覺一句。

---

### Q1 · 短標題

**答：** …

*解釋：* …

---
```

最後一題後不加 `---`。請寫入時答案一併落檔。