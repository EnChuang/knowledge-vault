---
title: (For Reader) Agent 指令範本
tags:
  - 方法論/知識庫
  - 方法論/Bootstrap
  - 讀者/For Reader
created: 2026-06-28
updated: 2026-07-06
---

# (For Reader) Agent 指令範本

> **給讀者複製貼上**。行為由 **`AGENTS.md`**（自動）+ **kv-* Skill**（觸發）負責。種子版本：**2026-07-06-v18**。

**前提**：庫根有 `AGENTS.md`、`Bootstrap.md`、`MEMORY.md`、`skills/`；終端 **工作目錄＝庫根**；在庫根執行 `grok`；**開新對話**。

**Skill 路徑**：kv-* 須在 `{庫根}/.grok/skills/`（建庫時由指令 ① 複製）。**不必**放在 `C:\Users\…\.grok\skills\`。詳見 **01 開箱導覽**。

---

## 指令 ①：完整建立知識庫架構（必跑）

```
這個資料夾有 AGENTS.md、Bootstrap.md、MEMORY.md、skills/。工作目錄是庫根。

請載入 kv-bootstrap Skill，依 Bootstrap.md B0→B7：

1. 建立 B1 目錄（含 MEMORY.md、Project/_DailyChange/DailyChange.md 種子）
2. 複製 skills/kv-*/ 到庫根 .grok/skills/（必須；勿覆寫使用者 ~/.grok/skills/ 內建 Skill）
3. 建立四 L1 Canon（Grok→MOC→Project→Source）；若本開箱包無詳盡 Canon，從種子建 MRC 並註明可後續對齊完整庫
4. B7 驗收回報（含 .grok/skills/ 下 14 包 kv-*，含 kv-memory、kv-palette）
5. 列出庫根檔案樹

未通過驗收前不要寫 Project 筆記。
```

---

## 指令 ②：建立第一個專題

```
架構已建完。請依 AGENTS 載入 kv-moc、kv-project、kv-flow。

建立專題「{你的專題名}」：
1. 與我確認專題名與範圍（一句話）
2. 出最小 {專題名} — MOC.md 草稿
3. 我說「請寫入」後才建檔
```

---

## 指令 ③：整理子主題筆記

```
請載入 kv-project、kv-moc、kv-flow、kv-method（輕量審查）。

專題「{專題名}」子主題「{子主題名}」：先草稿，符合白皮書與讀者自測。
我說「請寫入」後跑完整交付審查再寫入並同步 MOC。
```

---

## 指令 ④：引用 Source

```
請載入 kv-source、kv-project、kv-flow。

來源：{連結或 Source/ 路徑}
引讀五步：讀完→大綱→對齊→蒸餾→自測。未請寫入前只草稿。
```

---

## 指令 ⑤：更名或改規則

```
請載入 kv-rename 或 kv-rules-sync、kv-flow、kv-method（完整交付審查）。

任務：{舊名→新名 或 規則變更}
1. 全庫 grep → 待改清單（含 skills、Bootstrap、建庫開箱）
2. 我說「請寫入」後才改檔
3. 同步 Skill + Bootstrap 種子；改 skills/ 後跑 sync_package.py
4. 再 grep 殘留
```

---

## 指令 ⑥：掃描／補 wikilink

```
請載入 kv-link-scan、kv-link、kv-flow。

1. python skills/kv-link-scan/scripts/scan_unlinked.py
   （可選 --topic "{專題名}"）
2. 我說「請寫入」後：
   python skills/kv-link-scan/scripts/apply_unlinked.py
3. 再跑 scan 確認
```

---

## 指令 ⑦：全庫健檢／打包前

```
請載入 kv-audit、kv-rules-sync、kv-method（完整交付審查）。

跑 G1–G10 健檢報告。G9 須對齊 建庫開箱（打包用）/ 與庫根。
未請寫入前不改檔。G9 待修清零後再複製開箱包給他人。
```

---

## 指令 ⑧：新安裝後確認 Skill（建庫完必跑）

```
請依 AGENTS.md：
1. 列出本庫應存在的 14 個 kv-* Skill 名稱（含 kv-memory、kv-palette）
2. 確認庫根 .grok/skills/ 下各有 SKILL.md（不必檢查 ~/.grok/skills/）
3. 說明我下一個「請寫入 Project」任務會載入哪些 Skill、依什麼順序
4. 若 .grok/skills/ 缺失，從 skills/ 複製並回報
```

---

## 指令 ⑨：同步 Skill 與開箱包（完整庫維護者）

```
請載入 kv-rules-sync、kv-flow、kv-method（完整交付審查）。

已改 skills/kv-*/ 或 AGENTS.md：
1. python skills/kv-link-scan/scripts/sync_package.py
2. 確認同步到庫根 .grok/skills/ 與 建庫開箱（打包用）/建庫開箱（打包用）/
3. 簡報 G9 相關項是否對齊
```

---

## 指令 ⑩：階段性收工（更新 AI 交班）

```
今天先這樣。請載入 kv-memory，詢問我是否更新 MEMORY.md。
我同意後才寫入；研究正文仍在 Project/，交付紀錄在 DailyChange。
```

---

## 常見狀況

| 狀況 | 貼給 Agent |
|------|------------|
| 剛建庫／新電腦 | 指令 ⑧ |
| 確認 Skill | `請依 AGENTS 列出本任務應載入的 kv-* Skill。` |
| 只討論 | `只草稿，不請寫入。` |
| 補連結 | 指令 ⑥；預設只報告 |
| 改 Skill 後 | 指令 ⑨ |
| 打包給別人 | 指令 ⑦；G9 通過後再複製本夾 |
| AI 找不到 kv-* | 確認 cd 庫根 + `.grok/skills/` 存在；貼指令 ⑧ |
| 今天先告一段落 | 指令 ⑩ |