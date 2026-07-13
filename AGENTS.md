# 知識庫 — L0 索引（Skill 驅動）

本檔為 Grok Session **唯一常駐載入**的規則入口。執行細節在 **kv-* Skill**；Canon 全文在庫根 `*_rules.md`（Skill 觸發時才讀）。

**可重現性**：空庫僅有本檔 → 載入 **kv-bootstrap** Skill，讀 `Bootstrap.md` B0→B7。種子版本：**2026-07-06-v18**。

---

## 本實例設定

| 項目 | 值 |
|------|-----|
| 顯示名稱 | Knowledge Vault |
| 庫根目錄 | 含 `AGENTS.md` 的資料夾（Grok cwd） |
| Harness | Grok Build（庫根啟動 `grok`） |
| Skill 路徑 | `skills/`（打包用）、`.grok/skills/`（庫內自動發現）、`~/.grok/skills/`（全域） |

---

## 啟動協議

**優先序**：用戶指令 ＞ 專項 Skill／Canon ＞ 本檔。

### 啟動前置

| 檢查 | 若缺失 | 動作 |
|------|--------|------|
| 四 L1（`Grok_rules`、`MOC_rules`、`Project_rules`、`Source_rules`） | 任一不存在 | **kv-bootstrap** → `Bootstrap.md` B0→B7 |
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
| **kv-project** | 知識長文、Ebook §12、讀者自測、標籤、分段 | 子主題整理、Ebook 章節、寫入 Project |
| **kv-moc** | MOC 四段、M1–M10 | 讀寫 MOC、寫入子筆記 |
| **kv-source** | 引讀五步、Ebook §12 預設、圖片 | 引用 Source、Ebook 引讀蒸餾 |
| **kv-link** | wikilink 兩類型、高頻節點 | 寫入含連結、更名後連結 |
| **kv-link-scan** | 詞彙掃描、未連結節點報告／請寫入套用 | 掃描連結、補 wikilink、專有名詞超連結 |
| **kv-rename** | 更名／搬移全庫對照 | 專題／筆記／Source 更名 |
| **kv-audit** | G1–G10 全庫健檢 | 健檢、打包前 |
| **kv-rules-sync** | L0／L1 對照、種子同步 | 寫入規則、改 L1 |
| **kv-bootstrap** | B0–B7 建庫 | 空庫、重置規則體系 |
| **kv-palette** | 配色查詢表去重讀寫 | 配色查詢、新增色板、PPT／畫圖取色 |
| **kv-rebalance** | 同專題新 Source／要點增量後重劃筆記邊界與 MOC | 重平衡、重新分類、地圖重排、專題偏重單源 |

Canon 對照：`Grok_rules`↔kv-flow+kv-link+kv-link-scan+kv-audit；`Project_rules`↔kv-project+kv-rename+kv-palette；`MOC_rules`↔kv-moc+kv-rebalance；`Source_rules`↔kv-source（增量整合→kv-rebalance）。

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
| 掃描／補 wikilink | kv-method（輕量）→ kv-link-scan → kv-link；請寫入 → 完整交付 + kv-flow |
| 全庫健檢／打包前 | kv-method（完整交付）→ kv-audit → kv-rules-sync |
| 空庫／重置 | kv-bootstrap |
| 配色查詢／新增色板 | kv-method → **kv-palette** → kv-flow；請寫入 → 完整交付 |
| **專題重平衡**（同專題新 Source／地圖不均） | kv-method → **kv-rebalance** → kv-source（若新源）→ kv-project → kv-moc → kv-rename（若拆併更名）；請寫入 → 完整交付 + kv-flow |
| 新領域 | 本檔 → 對應 Skill |

未說「請寫入」→ **只出草稿**（kv-flow §1）。

---

## L1 分類（Canon 歸檔用）

| 軸 | Canon 檔 | 對應 Skill |
|----|----------|------------|
| 流程 | [[Grok_rules]] | kv-flow, kv-link, kv-audit |
| 產出 | [[Project_rules]] | kv-project, kv-rename, kv-palette |
| 來源 | [[Source_rules]] | kv-source |
| 地圖 | [[MOC_rules]] | kv-moc, kv-rebalance |

新建規範 → 寫 Canon + 同步 Skill + `Bootstrap.md` 種子（**kv-rules-sync**）。

---

## 知識庫目錄

| 路徑 | 內容 | AI 常駐？ |
|------|------|----------|
| `AGENTS.md` | L0 索引 | **是** |
| `MEMORY.md` | 僅 AI 之 Session 交班（機器格式） | 否（**kv-memory** 按需） |
| `Bootstrap.md` | 建庫種子 | 僅 kv-bootstrap |
| `skills/kv-*/SKILL.md` | 執行規則 | 依任務觸發 |
| `*_rules.md` | Canon 全文 | Skill 要求時 |
| `Project/` | 筆記、MOC | 否 |
| `Project/_DailyChange/DailyChange.md` | 完整交付審查之當期日誌（單檔輪替） | 否 |
| `Project/_Architecture/Architecture-Status.md` | Harness vs 業界、架構決策（單檔） | 否 |
| `Project/配色查詢表.md` | 8 色 palette 累積查詢（**kv-palette**） | 否 |
| `Source/` | 原文 | 否 |
| `建庫開箱（打包用）/` | 開箱包 | G9 對照 |

---

## L0 僅管這些

- 規則正文用「**知識庫**」；顯示名稱見上表
- 須遵守的規範：L0 + Skill + Canon（不堆進 `Project/`）
- 改 Canon → 同步 Skill + `Bootstrap.md` 種子
- 改 `skills/` 或 L0 涉架構 → **kv-rules-sync** + `python skills/kv-link-scan/scripts/sync_package.py`（→ `.grok/skills/` + 開箱包）
- 庫根啟動 `grok`；先跑啟動前置
- 「請寫入」→ **kv-flow** §3 → §4；交付前 **kv-method** 完整交付審查
- 階段性收工（今天先這樣、先告一段落等）→ **kv-memory** 詢問是否更新 `MEMORY.md`

**Bootstrap 全文** → `Bootstrap.md`（勿塞回本檔以省 token）。