# Knowledge Vault

**用 AI 幫你寫 Obsidian 知識庫——先講清規則，再動手改檔。**

[![Seed](https://img.shields.io/badge/seed-2026--07--06--v18-blue)](./Bootstrap.md)
[![Skills](https://img.shields.io/badge/kv--skills-14-informational)](./skills/)
[![Harness](https://img.shields.io/badge/harness-Grok%20Build-black)](https://x.ai/)

> 一份**可重現的知識庫架構包**：放進空資料夾 → 庫根啟動 Grok → 貼建庫指令 → 長出與設計相同的分層規則、14 個執行 Skill，以及「草稿／請寫入」安全閘門。

研究正文進 `Project/`，規則留在庫根，原文進 `Source/`。  
**AI 讀規則做事；你讀筆記與變更日誌。**

---

## Highlights

- **不會亂改你的庫** — 沒說「請寫入」就只出草稿  
- **規則可打包帶走** — Bootstrap + 14 Skill，空機也能重建  
- **專題地圖（MOC）** — 筆記樹、文獻、待延伸一眼看懂  
- **原文與筆記分離** — PDF／書／圖在 `Source/`，筆記用連結指回  
- **跨對話交班** — AI 有 `MEMORY`；你有空白的 `DailyChange` 記出貨  
- **全庫可健檢** — G1–G10（連結、MOC、開箱對齊等）

---

## 目錄

- [這包解決什麼問題？](#這包解決什麼問題)
- [功能一覽](#功能一覽你裝好之後能做什麼)
- [五分鐘開始](#五分鐘開始)
- [日常怎麼用](#日常怎麼用最重要的三句話)
- [誰讀什麼檔](#誰讀什麼檔)
- [本包含什麼](#本包含什麼)
- [架構長什麼樣](#架構長什麼樣)
- [規則與 Skill](#規則與-skill速查)
- [版本與更新](#版本與更新)
- [常見問題](#幾個你可能會問的問題)
- [授權](#授權)

---

## 這包解決什麼問題？

| 痛點 | 本包做法 |
|------|----------|
| AI 亂寫檔、發明文獻 | 沒說「**請寫入**」→ 只草稿；引讀須對齊 `Source/` |
| 品質不穩 | 重大寫入前**完整交付審查** → 寫進你自己的 `DailyChange` |
| 跨對話失憶 | `MEMORY.md` 給 AI 交班（你不必讀）；正文在 `Project/` |
| 無法重現／給別人 | `Bootstrap` + 本包 Skill → 空庫重建同一套規則 |

---

## 功能一覽（你裝好之後能做什麼）

### 安全與品質

- **草稿預設** — 討論、整理、引讀都可先只看草稿  
- **請寫入閘門** — 你同意後才改檔；寫入前後有檢查清單  
- **完整交付審查** — 重大交付 12 節對抗審查；致命問題會停手  
- **你的變更日誌** — `Project/_DailyChange/DailyChange.md` 開箱時為**空白**

### 知識怎麼長

- **專題 MOC** — `{專題} — MOC.md`：簡介、筆記樹、文獻、待延伸  
- **白皮書式筆記** — 可讀段落，不是碎卡片堆  
- **讀者自測** — 整理後 10–20 題方便複習  
- **電子書／長文蒸餾** — 預設章節格式（公式＋註解＋比喻、考點與答案）  
- **原文與筆記分離** — `Source/literature|Ebook|Image`

### 連結與維護

- **wikilink 規範** — 知識節點 vs Source 路徑分開  
- **掃描漏連** — 找出尚未 `[[連結]]` 的專有名詞  
- **更名全庫更新** — 改檔名／專題名時對照整庫  
- **健檢 G1–G10** — 連結、MOC、圖片、規則一致性等  

### 跨對話記憶

- **三分流** — 正文 `Project/` ／ 人看 `DailyChange` ／ AI 交班 `MEMORY`  
- **收工先問** — 「今天先這樣」→ AI 先問要不要更新 MEMORY  

### 可攜與可重現

- **14 個 kv-\* Skill** — 按任務載入，不一次塞滿上下文  
- **Bootstrap B0–B7** — 空夾長出四 Canon + 目錄  
- **規則與正文分離** — 改研究筆記 ≠ 改 AI 憲法  

逐步指令與路徑細節 → [`(For Reader) 01–03`](#建議閱讀順序)。

---

## 五分鐘開始

### 你需要

1. **Grok Build**（或能讀庫根 `AGENTS.md` + `.grok/skills/` 的相容環境）  
2. 本倉庫**全部檔案**（至少：`AGENTS.md`、`Bootstrap.md`、`MEMORY.md`、`skills/`）  
3. 一個空資料夾當**庫根**

### 步驟

```text
1. Clone 或下載本倉庫 → 內容放到空資料夾（該夾＝庫根）
2. 終端機 cd 到庫根
3. 執行 grok，開新對話
4. 打開 (For Reader) 03 → 貼上【指令 ①】完整建庫
5. 確認驗收：四 *_rules.md、.grok/skills/ 下 14 個 kv-*
6. 貼【指令 ②】開第一個專題（說「請寫入」後才建檔）
```

### 成功長這樣

- 庫根有 `Grok_rules.md`、`MOC_rules.md`、`Project_rules.md`、`Source_rules.md`  
- `{庫根}/.grok/skills/` 有 **14** 個 `kv-*/SKILL.md`  
- `Project/`、`Source/` 骨架就緒  
- `DailyChange.md` 仍是**空白**（等你第一次重大交付）

**請在庫根啟動 `grok`。** Skill 在庫內 `.grok/skills/`，不必塞進 `~/.grok/skills/`。

---

## 日常怎麼用（最重要的三句話）

1. **先討論、後落盤** — 沒說「請寫入」＝ AI 不改檔  
2. **研究寫在專題裡** — `Project/{專題}/` + `{專題} — MOC.md`  
3. **收工可以交班** — 「今天先這樣」→ AI 問要不要更新 `MEMORY.md`

| 你想… | 你可以這樣說／做 |
|--------|------------------|
| 弄懂概念 | 直接問；草稿即可 |
| 討論變筆記 | 確認後說 **「請寫入」** |
| 讀 PDF／書 | 檔放 `Source/`，請 AI 引讀蒸餾 |
| 開新主題 | 專題名 → MOC 草稿 → 「請寫入」 |
| 改名 | 舊名→新名，全庫對照後再「請寫入」 |
| 掃連結 | 「掃描連結」；套用再說「請寫入」 |
| 看出貨紀錄 | 打開 `Project/_DailyChange/DailyChange.md` |
| 配色 | 配色查詢 → `Project/配色查詢表.md` |

---

## 誰讀什麼檔？

```text
你 ──► README、For Reader 01–03、DailyChange、Project 筆記
AI ──► AGENTS.md（每次）→ skills/kv-*
       MEMORY.md（交班；你不必讀）
       *_rules.md（需要完整條文時）
```

| 檔案 | 給誰 | 做什麼 |
|------|------|--------|
| `README.md` | 你 | 使用說明（本檔） |
| `(For Reader) 01–03` | 你 | 導覽、一頁紙、可複製指令 |
| `Project/**` | 你 + AI | 專題正文與 MOC |
| `DailyChange.md` | **你為主** | 重大交付 Pass／改了什麼 |
| `MEMORY.md` | **僅 AI** | 跨對話交班 |
| `AGENTS.md` / `skills/` | AI | 入口與執行手冊 |
| `Bootstrap.md` | AI（建庫） | 種子 B0–B7 |
| `Source/**` | 你放、AI 引 | 原文 |

---

## 本包含什麼？

```text
.
├── README.md
├── CHANGELOG.md              ← 版本變更紀錄
├── LICENSE
├── .gitignore
├── (For Reader) 01 開箱導覽.md
├── (For Reader) 02 架構一頁紙.md
├── (For Reader) 03 Agent 指令範本.md
├── AGENTS.md                 ← AI 常駐 L0
├── Bootstrap.md              ← 建庫種子
├── MEMORY.md                 ← AI 交班種子（空熱區）
├── skills/kv-*/              ← 14 包執行規則
└── Project/_DailyChange/
    └── DailyChange.md        ← 空白變更日誌（給你用）
```

建庫後還會多：四份 `*_rules.md`、`Source/` 子目錄、`.grok/skills/`（由 `skills/` 複製）。

---

## 架構長什麼樣？

```text
你的口頭指令（最高優先）
    │
    ▼
AGENTS.md ──────── L0：去找哪個 Skill
    ├── skills/kv-* ── 怎麼做（按需載入）
    ├── *_rules.md ─── Canon 全文（需要時才讀）
    └── Bootstrap.md ─ 空庫重置

Project/        研究正文 + MOC
Source/         原文
MEMORY.md       僅 AI 交班
DailyChange.md  你的出貨紀錄
```

```text
對話結束 ──蒸餾──► MEMORY.md      （給下一輪 AI）
              │
              └──審查──► DailyChange （給你看）
專題研究 ────────────► Project/    （長期知識）
```

---

## 規則與 Skill（速查）

| Canon | 管什麼 |
|-------|--------|
| `Grok_rules.md` | 寫入、連結、健檢 |
| `Project_rules.md` | 筆記格式、更名、Ebook 章節 |
| `MOC_rules.md` | 專題地圖 |
| `Source_rules.md` | 原文引讀 |

| Skill | 一句話 |
|-------|--------|
| **kv-method** | 輕量／完整交付審查 |
| **kv-flow** | 請寫入前後檢查 |
| **kv-project** | 整理筆記、自測、章節格式 |
| **kv-moc** | 專題 MOC |
| **kv-source** | 引讀原文 |
| **kv-link** / **kv-link-scan** | 連結規則／掃描補連 |
| **kv-memory** | 讀寫 MEMORY |
| **kv-token** | 長文與讀取預算 |
| **kv-rename** | 更名全庫對照 |
| **kv-audit** | G1–G10 健檢 |
| **kv-rules-sync** | 規則與種子同步 |
| **kv-bootstrap** | 空庫建架構 |
| **kv-palette** | 配色查詢表 |

不必背名字：用白話說需求，AI 依 `AGENTS.md` 載入。

---

## 版本與更新

| 名稱 | 用途 |
|------|------|
| **種子** `2026-07-06-v18` | 寫在 `AGENTS.md`／`Bootstrap.md`：規則體系內部代次 |
| **Git 標籤** `v1.0.0` | GitHub Release 給下載者的公開版本（[語義化版本](https://semver.org/lang/zh-TW/)） |

變更摘要見 **[CHANGELOG.md](./CHANGELOG.md)**。  
維護者更新流程與 commit 格式見下方「給維護者」與倉庫說明；一般使用者：`git pull` 或下載新 Release 後，對照 CHANGELOG 決定是否重跑 Bootstrap／只覆蓋 `skills/`。

---

## 幾個你可能會問的問題

**一定要 Grok 嗎？**  
本包依 Grok Build 的 Skill 發現路徑設計。其他 Agent 若能讀 `AGENTS.md` 與 Skill 目錄可嘗試，須自行驗證。

**DailyChange 為什麼是空的？**  
那是**你的**出貨日誌，不帶原作者紀錄。第一次重大「請寫入」後才會開始寫。

**要讀 MEMORY.md 嗎？**  
不必。看 `Project/` 與 `DailyChange` 即可。

**Skill 要複製到 `C:\Users\我\.grok\skills\` 嗎？**  
**不必。** 建庫時複製到**庫根** `.grok/skills/` 即可。

**可以改規則嗎？**  
可以。改完應同步 Bootstrap 種子（`kv-rules-sync`）。建議先用預設流程一陣子再改。

---

## 建議閱讀順序

1. **本 README**（使用說明）  
2. **`(For Reader) 02 架構一頁紙`**  
3. **`(For Reader) 03`** — 複製指令給 AI  
4. 需要細節 → **`(For Reader) 01`**

---

## 授權

見 [LICENSE](./LICENSE)。（預設 MIT：可自由使用、修改、再發布；請保留著作權聲明。）

---

## 給維護者（一句）

改 `skills/` 或 L0 後，在**完整庫**跑同步腳本、確認開箱包 `MEMORY`／`DailyChange` 仍為種子、更新 `CHANGELOG.md`、再 `git tag` + GitHub Release。細節見你完整庫 README 的打包說明與本專案的 commit 慣例（Conventional Commits）。
