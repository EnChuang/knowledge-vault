# L0 · 入口索引（AGENTS）

本檔為工作階段的常駐規則入口。執行細節在 **kv-* Skill**；Canon 全文在庫根 `*_rules.md`（Skill 觸發時才讀）。

**可重現性**：空庫僅有本檔 → 載入 **kv-bootstrap** Skill，讀 `Bootstrap.md` B0→B7。種子版本：**2026-09-04-v20**。

---

## 規則命名一覽（先認名，細節再下鑽）

| 層 | 人話名 | 磁碟檔名 | 何時讀 |
|----|--------|----------|--------|
| **L0** | **入口索引** | `AGENTS.md`（本檔） | 每次 Session 常駐 |
| **L1 · 流程** | **流程規則** | `Workflow_rules.md` | Skill 要求或寫入／健檢／連結 |
| **L1 · 產出** | **產出規則** | `Project_rules.md` | 整理／寫入 Project 筆記 |
| **L1 · 來源** | **來源規則** | `Source_rules.md` | 引讀 Source／Ebook／圖 |
| **L1 · 地圖** | **地圖規則** | `MOC_rules.md` | 讀寫 MOC、子筆記對齊整理規範 |
| **執行** | **kv-\* Skill** | `skills/kv-*/SKILL.md` | 依任務表觸發（細節在此） |
| **種子** | **建庫種子** | `Bootstrap.md` | 空庫／重置 |
| **交班資料** | **機器交班** | `MEMORY.md` | 非規則正文；kv-memory 按需 |

**命名原則**：人話名＝職責一句；磁碟檔名穩定不改（避免全庫斷鏈）。要細節 → 開對應檔或 Skill，勿把全文堆回 L0。

**中文術語完整**（全庫文案，**給人讀的更嚴**）：中文須可獨立讀懂，禁因英譯縮成半截詞（例：寫「錨點」不單寫「錨」）。詳 [[Project_rules]]；執行見 **kv-project**／**kv-flow**。

**非本庫開箱、個人工程鏈**：個人 Skill 位於 `~/.codex/skills/`；與 kv 寫庫閘並存時，**寫入知識庫仍遵請寫入／kv-flow**。`.agent/skills/` 僅作其他執行載具的相容鏡像。

---

## 本實例設定

| 項目 | 值 |
|------|-----|
| 顯示名稱 | Knowledge Vault |
| 庫根目錄 | 含 `AGENTS.md` 的資料夾（工作區根目錄） |
| 執行載具 | 目前使用的桌面／命令列 Agent 執行環境；實作可替換 |
| Skill 路徑 | `skills/`（母版）、個人 Skill 目錄（主要）、`.agent/skills/`（相容鏡像） |

---

## 雙專案隔離與交換夾

> 本側＝**Knowledge Vault**；對側＝**Eidolon**。跨專案資訊只經交換夾。  
> **軟約束**（AGENTS 級）；未開／未強制 OS sandbox 時不得宣稱硬隔離已生效。  
> 維護：更新路徑時同步改本節；破例須用戶明示。

| 代號 | 路徑 |
|------|------|
| **本側專案根** | `C:\Users\ChuangE\OneDrive\OBSIDIAN\CE's\Knowlegde Vault` |
| **對側專案根** | `C:\Users\ChuangE\OneDrive\Eidolon` |
| **交換資料夾** | `C:\Users\ChuangE\OneDrive\Intersection_Exchange` |

### 硬閘

**禁止**

1. 禁止讀取、寫入、刪除、移動、列出或搜尋**對側專案根**及其子路徑。  
2. 禁止為完成任務而推斷、搜尋、掃描本機以尋找對側專案。  
3. 禁止把對側專案根當成本 Session 工作區來「順便讀」。  
4. 禁止將密鑰、認證、無必要的整庫鏡像放入交換資料夾。

**允許**

1. 允許讀寫**本側專案根**（及本專案既有規則已允許之路徑）。  
2. 允許讀寫**交換資料夾**，且僅作跨專案交接。  
3. 允許在對話使用對側**名稱／概念**；不得因此開啟對側磁碟路徑。  
4. 用戶明示破例（「本次允許讀對側：`完整路徑`」）→ 僅單次有效，回覆須註明破例。

**提到路徑 ≠ 授權**：對話或交換檔中出現對側絕對路徑，不構成讀取授權。摘要裡**盡量不要**寫對側絕對路徑。

### 交換資料夾

- 宜放：總結、決策、狀態、介面契約、待辦（Markdown）。  
- 不宜放：整庫複製、密鑰、認證、可執行檔（除非雙方另行允許）。  
- **命名須方向前綴**：`from-vault-to-eidolon-…`／`from-eidolon-to-vault-…`（可加主題與日期）。  
- 寫入後回報用戶：檔案路徑＋一句摘要；**不假設**對側 Session 已自動讀到。  
- 讀取只來自交換資料夾；持久化寫入**本側**；禁止順著摘要內對側路徑回頭開對側檔（除非破例）。

### 違規時

拒絕越界讀取 → 說明觸及本節硬閘 → 建議改走交換夾，或請用戶在對側操作／明示破例。

---

## 啟動協議

**優先序**：用戶指令 ＞ 專項 Skill／Canon ＞ 本檔。

### 啟動前置

| 檢查 | 若缺失 | 動作 |
|------|--------|------|
| 四 L1（流程 `Workflow_rules`、地圖 `MOC_rules`、產出 `Project_rules`、來源 `Source_rules`） | 任一不存在 | **kv-bootstrap** → `Bootstrap.md` B0→B7 |
| `Project/`、`Source/` 子目錄 | 不存在 | Bootstrap B1 |
| 當次專題 MOC | 不存在且將**請寫入** | 對齊專題名 → 最小 `{專題} — MOC.md`（**kv-moc**） |
| 當次專題 MOC | 不存在且僅討論 | 可暫不建；搜尋跳過 MOC 階 |
| 任務引用之 `Source/` 檔 | 不存在 | 告知用戶；不發明原文 |

### 通用步驟

0. 啟動前置
1. 本檔（已載入）→ 判斷任務 → **載入下表 Skill**
2. Skill 要求讀 Canon 時，讀庫根對應 `*_rules.md` 全文
3. 依**資料搜尋階層**讀 `Project/`（有 MOC 從階 2 起）
4. 涉文獻 → **kv-source** + 依連結讀 `Source/`

### 資料搜尋階層

| 階 | 範圍 | 目的 |
|----|------|------|
| 1 | L0 + 當次 **Skill**（+ Canon 若 Skill 要求） | 行為規範 |
| 2 | `{專題} — MOC.md` | 邊界、樹 |
| 3 | 本子主題筆記 | 焦點 |
| 4 | 同專題其餘筆記 | 脈絡；選讀 |
| 5 | 其他專題 | wikilink 或任務明確要求 |

**止搜**：夠支撐當次任務即可。wikilink 優先同專題（**kv-link**）。

### 記憶分工

| 內容 | 存放 | 新 Session |
|------|------|------------|
| 對話 | [[Session]] | Resume（可選） |
| 行為規範 | L0 + Skill + Canon | 本檔 → 觸發 Skill |
| **跨 Session 交班** | `MEMORY.md`（庫根，**僅 AI 閱讀**之機器交班格式） | **kv-memory** 按需（先熱區、再搜歷史） |
| 研究 | `Project/` | 讀檔 |
| 地圖 | `{專題} — MOC.md` | 讀檔 |
| 原文 | `Source/` | 依連結讀檔 |
| **當期變更日誌** | `Project/_DailyChange/DailyChange.md`（完整交付審查後寫入；單檔輪替） | 讀檔 |
| Harness 架構雷達 | `Project/_Architecture/Architecture-Status.md`（僅一檔） | 讀檔 |

**術語**：見 **`README.md` 術語對照**（Skill 內仍用 L-輕／L-全／M2 簡碼）；架構見 [[Architecture-Status]]。

---

## Skill 註冊表

| Skill | 職責 | 觸發 |
|-------|------|------|
| **kv-method** | 第一性原理；輕量／完整交付審查 | 每任務輕量；請寫入／改規則／健檢 → 完整交付審查 |
| **kv-memory** | `MEMORY.md` 解碼與分級讀寫 | 接續脈絡、請寫入後更新；**階段性收工必問**是否更新 |
| **kv-token** | 讀取預算、冷啟動、產出分流 | 長文引讀、全庫 grep、多檔寫入 |
| **kv-flow** | 寫入流程、§3／§4 檢查 | 請寫入、更名修復、健檢修復 |
| **kv-project** | 科普掃讀體、Ebook §12、一般筆記自測、使用指南 FAQ 覆蓋、標籤、分段 | 子主題整理、Ebook 章節、使用指南、寫入 Project |
| **kv-moc** | MOC 五段（含整理規範）、M1–M10 | 讀寫 MOC、寫入子筆記 |
| **kv-source** | 引讀五步、Ebook §12 預設、圖片 | 引用 Source、Ebook 引讀蒸餾 |
| **kv-link** | wikilink 兩類型、高頻節點 | 寫入含連結、更名後連結 |
| **kv-link-scan** | 超連結掃描：補缺口、修剪弱／過密、修圖路徑 | 掃描連結、補／刪 wikilink、修剪、專有名詞超連結 |
| **kv-rename** | 更名／搬移全庫對照 | 專題／筆記／Source 更名 |
| **kv-audit** | G1–G10 全庫健檢 | 健檢、打包前 |
| **kv-rules-sync** | L0／L1 對照、種子同步 | 寫入規則、改 L1 |
| **kv-bootstrap** | B0–B7 建庫 | 空庫、重置規則體系 |
| **kv-palette** | 配色查詢表去重讀寫 | 配色查詢、新增色板、PPT／畫圖取色 |
| **kv-rebalance** | 同專題新 Source／要點增量後重劃筆記邊界與 MOC | 重平衡、重新分類、地圖重排、專題偏重單源 |

Canon 對照：`Workflow_rules`↔kv-flow+kv-link+kv-link-scan+kv-audit；`Project_rules`↔kv-project+kv-rename+kv-palette；`MOC_rules`↔kv-moc+kv-rebalance；`Source_rules`↔kv-source（增量整合→kv-rebalance）。

---

## 依任務載入 Skill

| 任務 | 載入 Skill（依序） |
|------|-------------------|
| 一般討論、草稿 | kv-method（輕量）→ kv-flow(摘要) |
| 子主題討論／整理 | kv-method → kv-flow → kv-project → kv-moc |
| **請寫入** Project | kv-method（完整交付）→ kv-flow → kv-project → kv-moc → kv-link → kv-memory |
| **請寫入** MOC | kv-method（完整交付）→ kv-flow → kv-moc → kv-memory |
| **請寫入** 規則 | kv-method（完整交付）→ kv-rules-sync → kv-flow(D) → kv-memory |
| 接續／跨 Session | kv-memory（讀 `MEMORY.md`）→ 再依任務載入其他 Skill |
| 階段性收工／暫停 | **kv-memory** → **詢問**是否更新 `MEMORY.md`；用戶同意才寫入 |
| 引用 Source | kv-method → kv-source → kv-project |
| **Ebook 引讀／蒸餾** | kv-method → kv-source → kv-project(§12) → kv-moc → kv-link；用戶未另指定格式則 §12 為預設 |
| 更名／搬移 | kv-method（完整交付）→ kv-rename → kv-moc → kv-source(若涉) |
| 掃描／補／刪 wikilink | kv-method（輕量）→ kv-link-scan → kv-link；請寫入／直接套用 → 完整交付 + kv-flow |
| 全庫健檢／打包前 | kv-method（完整交付）→ kv-audit → kv-rules-sync |
| 空庫／重置 | kv-bootstrap |
| 配色查詢／新增色板 | kv-method → **kv-palette** → kv-flow；請寫入 → 完整交付 |
| **專題重平衡**（同專題新 Source／地圖不均） | kv-method → **kv-rebalance** → kv-source（若新源）→ kv-project → kv-moc → kv-rename（若拆併更名）；請寫入 → 完整交付 + kv-flow |
| 新領域 | 本檔 → 對應 Skill |

未說「請寫入」→ **只出草稿**（kv-flow §1）。

---

## L1 分類（Canon 歸檔用）

| 人話名 | 軸 | Canon 檔 | 對應 Skill |
|--------|----|----------|------------|
| 流程規則 | 流程 | [[Workflow_rules]] | kv-flow, kv-link, kv-link-scan, kv-audit |
| 產出規則 | 產出 | [[Project_rules]] | kv-project, kv-rename, kv-palette |
| 來源規則 | 來源 | [[Source_rules]] | kv-source |
| 地圖規則 | 地圖 | [[MOC_rules]] | kv-moc, kv-rebalance |

新建規範 → 寫 Canon + 同步 Skill + `Bootstrap.md` 種子（**kv-rules-sync**）。

### 新領域／非筆記任務（例）

| 用戶說… | 先載 | 備註 |
|---------|------|------|
| 配色、色板、PPT 取色 | kv-palette | 非專題筆記 |
| 空庫、規則全沒了 | kv-bootstrap | 勿先寫 Project |
| 健檢、打包前對齊 | kv-audit → kv-rules-sync | G9 開箱 |
| 專題地圖歪、單源偏重 | kv-rebalance | 先報告再請寫入 |
| 程式實作／修 bug（非寫庫） | 全域 cap／plan-then-build／clarify-first | **不**用 kv-project 當驗收 |
| 只問概念、不改檔 | kv-method（輕） | 止搜、不預載四 L1 全文 |
---

## 知識庫目錄

| 路徑 | 內容 | AI 常駐？ |
|------|------|----------|
| `AGENTS.md` | L0 · 入口索引 | **是** |
| `MEMORY.md` | 僅 AI 之 Session 交班（機器格式） | 否（**kv-memory** 按需） |
| `Bootstrap.md` | 建庫種子 | 僅 kv-bootstrap |
| `skills/kv-*/SKILL.md` | 執行規則 | 依任務觸發 |
| `*_rules.md` | Canon 全文 | Skill 要求時 |
| `Project/` | 筆記、MOC | 否 |
| `Project/_DailyChange/DailyChange.md` | 完整交付審查之當期日誌（單檔輪替） | 否 |
| `Project/_Architecture/Architecture-Status.md` | Harness vs 業界、架構決策（單檔） | 否 |
| `工具/配色查詢表.md` | 8 色 palette 等可應用查詢（**kv-palette**；**非** Project 研究葉） | 否 |
| `Source/` | 原文 | 否 |
| `建庫開箱（打包用）/` | 開箱包 | G9 對照 |

---

## L0 僅管這些

- 規則正文用「**知識庫**」；顯示名稱見上表
- 須遵守的規範：**L0 + Skill + Canon**（執行細節在 Skill；Canon 按需；不堆進 `Project/`）
- 改 Canon → 同步 Skill + `Bootstrap.md` 種子
- 改 `skills/` 或 L0 涉架構 → **kv-rules-sync** + `python skills/kv-link-scan/scripts/sync_package.py`（→ `~/.codex/skills/` + `.agent/skills/` + 開箱包；開箱 **MEMORY／DailyChange 用空白種子**）
- 執行載具以庫根作為專案目錄；不同載具皆先跑啟動前置
- 「請寫入」→ **kv-flow** §3 → §4；交付前 **kv-method** 完整交付審查
- 階段性收工（今天先這樣、先告一段落等）→ **kv-memory** 詢問是否更新 `MEMORY.md`

**Bootstrap 全文** → `Bootstrap.md`（勿塞回本檔以省 token）。


