---
title: Agent 指令範本
tags:
  - 方法論/知識庫
  - 方法論/Bootstrap
  - 讀者/For Reader
created: 2026-06-28
updated: 2026-07-12
---

# Agent 指令範本

**複製方塊裡的文字，貼進 Grok 對話。**  
行為由 `AGENTS.md` + kv-\* Skill 負責；你不必背 Skill 名。

種子：**2026-07-06-v18**

### 貼之前請確認

- 終端 **工作目錄＝庫根**（有 `AGENTS.md`）  
- 已在庫根執行 `grok`，且是**新對話**（建庫時）  
- 庫根有：`AGENTS.md`、`Bootstrap.md`、`MEMORY.md`、`skills/`  
- kv-\* 會進 `{庫根}/.grok/skills/`（指令 ① 會複製）；**不必**放使用者全域目錄  

路徑說明 → [01-開箱導覽](./01-開箱導覽.md)

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

專題「{專題名}」子主題「{子主題名}」：先草稿，符合知識長文（鉤子／命題／收束）與讀者自測。
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
1. 全庫 grep → 待改清單（含 skills、Bootstrap、docs、開箱相關路徑）
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

跑 G1–G10 健檢報告。開箱包／公開倉庫與庫根規則須對齊。
未請寫入前不改檔。對齊通過後再 push 或複製給他人。
```

---

## 指令 ⑧：新安裝後確認 Skill（建庫完建議跑）

```
請依 AGENTS.md：
1. 列出本庫應存在的 14 個 kv-* Skill 名稱（含 kv-memory、kv-palette）
2. 確認庫根 .grok/skills/ 下各有 SKILL.md（不必檢查 ~/.grok/skills/）
3. 說明我下一個「請寫入 Project」任務會載入哪些 Skill、依什麼順序
4. 若 .grok/skills/ 缺失，從 skills/ 複製並回報
```

---

## 指令 ⑨：同步 Skill（完整庫維護者）

```
請載入 kv-rules-sync、kv-flow、kv-method（完整交付審查）。

已改 skills/kv-*/ 或 AGENTS.md：
1. python skills/kv-link-scan/scripts/sync_package.py
2. 確認同步到庫根 .grok/skills/ 與公開開箱包目錄
3. 確認 MEMORY／DailyChange 種子未被個人 Session 覆寫
4. 簡報是否可發版
```

---

## 指令 ⑩：階段性收工

```
今天先這樣。請載入 kv-memory，詢問我是否更新 MEMORY.md。
我同意後才寫入；研究正文仍在 Project/，交付紀錄在 DailyChange。
```

---

## 速查

| 狀況 | 用 |
|------|-----|
| 剛建庫 | ① → ⑧ → ② |
| 只討論 | 說「只草稿，不請寫入」 |
| 補連結 | ⑥ |
| 打包／發版前 | ⑦ |
| 找不到 kv-\* | 確認庫根 + ⑧ |
| 收工 | ⑩ |

地圖 → [02-架構一頁紙](./02-架構一頁紙.md) · 首頁 → [README](../../README.md)
