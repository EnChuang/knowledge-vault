# Bootstrap 開箱（可重現規格）

> **使用情境**：空資料夾、或重置規則體系。由 **kv-bootstrap** Skill 載入本檔。建庫後 Canon 與 `skills/` 須與庫根實例對齊。種子版本：**2026-09-07-v21**。

## B0 建庫順序（必按序）

| 步 | 動作 | 產出 |
|----|------|------|
| 1 | 建立目錄骨架（B1） | 空資料夾 |
| 2 | 確認 `AGENTS.md`（L0）+ 本檔在庫根 | 索引 + 種子 |
| 3 | 複製 `skills/kv-*/` → 個人 Skill 目錄（主要）與庫根 `.agent/skills/`（相容鏡像） | Skill 可發現 |
| 4 | 依序建立 L1 種子：**工作流 → 地圖 → 產出 → 來源**（B3–B6） | 4 個 `*_rules.md` |
| 5 | 跑驗收（B7） | 通過／修正 |
| 6 | （可選）建 `MEMORY.md`、`Project/_DailyChange/DailyChange.md`、第一個專題 MOC | 實例檔 |

**勿跳步**：工作流 Canon 內 §3–§4 引用其他 L1；故工作流先建，其餘三檔依序補齊後再跑 B7。

## B1 目錄骨架

```text
{庫根}/
├── AGENTS.md
├── MEMORY.md              # 跨 Session 交班簿（kv-memory；非常駐）
├── Bootstrap.md
├── Workflow_rules.md
├── MOC_rules.md
├── Project_rules.md
├── Source_rules.md
├── skills/
│   └── kv-*/SKILL.md
├── .agent/skills/          # 自 skills/ 複製，其他執行載具的相容鏡像
├── Project/
│   ├── _DailyChange/      # 完整交付審查之當期日誌（非 Session 交班）
│   │   └── DailyChange.md
│   └── _Architecture/
│       └── Architecture-Status.md
└── Source/
    ├── literature/
    ├── Ebook/
    └── Image/
```

## B2 L1 檔頭慣例

| 檔案 | frontmatter | 檔頭引用塊 |
|------|-------------|------------|
| `Workflow_rules.md` | 無 | `> 規則層級：L1…` + Skill 對照 + 種子見本檔 B3 |
| 其餘 L1 | `title`、`tags`、`created` | 同上；衝突時以本檔 Canon 為準 |

每個 L1 必有**本檔目錄**表。執行時以 **kv-* Skill** 為準；Canon 供人讀與健檢對照。

### B2.5 種子與磁碟

| 狀態 | 以誰為準 |
|------|----------|
| **日常執行** | 磁碟 `*_rules.md` + `skills/` |
| **空庫重置** | 本檔種子 → 建 Canon |
| **改 L1 後** | 回寫本檔種子 + 同步 Skill（kv-rules-sync） |

## B3–B6 種子檔全文

以下四段為種子。**複製「開始↓」與「結束↑」之間全文**建立對應檔案。

---
**種子檔 `Workflow_rules.md` 開始 ↓**
---

> **人話名**：L1 · 流程規則　**檔名**：`Workflow_rules.md`  
> 先讀 [[AGENTS.md]]（L0 · 入口索引），執行見 **kv-flow**、**kv-link**、**kv-audit**。  
> 專項細節見各 L1；**專項優先於本檔簡述**。種子見 [[Bootstrap.md]] B3。

---

## 本檔目錄

| 章節 | 內容 |
|------|------|
| §0 啟動與搜尋 | Session 順序、資料搜尋階層（對齊 AGENTS「啟動協議」） |
| §1 核心原則 | 語言、證據、寫入、連結、規則歸屬 |
| §2 寫入流程 | 草稿到寫入 |
| §3 寫入前檢查 | 請寫入前清單 |
| §4 寫入後檢查 | 寫入後清單 |
| §5 內部連結 | Source vs 知識節點；掃描／補／修剪 → kv-link-scan |
| §6 L1 索引 | 專項對照 |
| §7 規則同步 | L0／L1 對照 |
| §8 討論延伸 | 結束後才問 |
| §9 全庫健檢 | G1–G10 |

---

## §0–§9

完整條文見庫根磁碟 `Workflow_rules.md`（Canon）。執行摘要：

- **啟動**：AGENTS 啟動前置；L1 缺 → kv-bootstrap
- **寫入**：未請寫入 → 草稿；請寫入 → kv-flow §3→§4
- **更名**：kv-rename；全庫 grep 舊名
- **健檢**：kv-audit G1–G10；打包前必 G9
- **方法論**：kv-method 輕量／完整交付審查
- **使用指南例外**：使用指南、操作指南、快速開始、開箱導覽、FAQ／疑難排解不寫讀者自測，改以「常見問題／疑難排解／操作檢查表」做流程覆蓋複核；一般知識筆記與 Ebook 自測閘門不變。

---
**種子檔 `Workflow_rules.md` 結束 ↑**
---

---
**種子檔 `MOC_rules.md` 開始 ↓**
---

---
title: MOC 規則
tags:
  - 方法論/MOC
  - 方法論/知識庫
created: 2026-07-02
---

> **規則層級**：L1 專項。執行見 **kv-moc**、**kv-rebalance**。種子見 [[Bootstrap.md]] B4。

---

## 本檔目錄

§1 定位 · §2 五段結構 · §3 各章節 · §4 M1–M10 · §5 維護 · §6 生長 · §7 專題重平衡 · §8 待延伸

---

## 摘要（MRC）

- 每專題 `{專題名稱} — MOC.md`；檔名＝`title`＝wikilink
- 五段：專題簡介、整理規範、筆記關係樹狀圖、文獻來源、待延伸
- 樹：巢狀 wikilink；**禁 mermaid**；只鏈已存在筆記
- M1–M10：見 kv-moc；M10 標籤無空格
- 不預填；待延伸僅延伸+請寫入後
- §7 同專題新 Source 增量：概念優先重劃 → **kv-rebalance**（勿只 append 舊卡）

完整條文見磁碟 `MOC_rules.md`。

---
**種子檔 `MOC_rules.md` 結束 ↑**
---

---
**種子檔 `Project_rules.md` 開始 ↓**
---

---
title: Project 筆記規則
tags:
  - 方法論/Project
  - 方法論/知識庫
created: 2026-07-02
---

> **規則層級**：L1 專項。執行見 **kv-project**、**kv-rename**。種子見 [[Bootstrap.md]] B5。

---

## 摘要（MRC）

- 整理筆記（非 Ebook）＝**科普掃讀**＋**完整句標題**（禁半截、禁後設括號注釋）；**葉題由蒸餾命題生成**，命名前先讀正文並抽出主體、主張與關係；準確優先於金句感，禁需解碼或拼接意象的隱喻標題；80% 覆蓋；認知科學校正清單
- **不重寫固定大綱**：Ebook §12、教科書／傳記章序、MOC 已定型版型；其餘自由葉標題須完整句、一眼懂
- 例外可冷寫：MOC、架構雷達、DailyChange、MEMORY、配色表、scaffold、明示清單
- **卡點譬喻**（§5）：先喻後理；長文多卡點 2–4 則；最低全文 1 則
- 掃讀節奏（§7）：宜表卡分鏡；禁長散文牆；連結有意義（§6）
- **Ebook 蒸餾預設**：§12（公式＋註解＋比喻、每章 10 題＋答案區）；公式島外人話一句
- 檔名＝`title`＝wikilink；禁泛稱；`tags` 無空格
- §10 更名全庫 grep；分段整理：只改指定段

完整條文見磁碟 `Project_rules.md`。

---
**種子檔 `Project_rules.md` 結束 ↑**
---

---
**種子檔 `Source_rules.md` 開始 ↓**
---

---
title: Source 規則
tags:
  - 方法論/Source
  - 方法論/知識庫
created: 2026-07-02
---

> **規則層級**：L1 專項。執行見 **kv-source**、**kv-rebalance**。種子見 [[Bootstrap.md]] B6。

---

## 摘要（MRC）

- `Source/literature/`、`Ebook/`、`Image/`；不按專題分夾
- 文獻 piped link 含副檔名；圖在 `Source/Image/`
- Ebook：未引用禁整本掃描；引讀蒸餾預設 [[Project_rules]] §12
- 引讀五步：讀完→大綱→對齊→蒸餾→覆蓋複核（一般筆記自測／指南 FAQ；Ebook 含 10/10 閘門與答案寫入）
- §6 同專題 Source 增量：新子域／舊卡過肥 → **kv-rebalance**

完整條文見磁碟 `Source_rules.md`。

---
**種子檔 `Source_rules.md` 結束 ↑**
---

## B7 驗收清單

| # | 檢查 | 通過條件 |
|---|------|----------|
| V1 | 檔案存在 | B1 所列 + `MEMORY.md` + `skills/kv-*/SKILL.md`（15 包，含 kv-rebalance） |
| V2 | 種子一致 | 四 L1 與 B3–B6 無缺章；Canon 可詳於 MRC |
| V3 | 交叉引用 | L1 內 `[[…]]` 指向存在檔；概念節點須明確標為虛擬節點，不冒充檔案 |
| V4 | L0 自洽 | `AGENTS.md` Skill 表與任務表可執行 |
| V5 | 職責 | Skill 執行、Canon 不與 Skill 衝突 |
| V6 | 試跑 | 依 AGENTS 任務表可載入 Skill 而不缺檔 |
| V7 | Skill 發現 | `~/.codex/skills/` 可見 kv-*；需要舊版相容時 `.agent/skills/` 亦須同步 |

## B9 種子 MRC 必備

| 檔案 | 必備 |
|------|------|
| **Workflow_rules** | 啟動；§3 A–F；§4 A–F；§5–§9；G1–G10；種子同步 |
| **MOC_rules** | 五段（含整理規範）；禁 mermaid；M1–M10；生長；§7 重平衡；待延伸 |
| **Project_rules** | 科普掃讀；大眾心理式標題；Ebook／教科書／傳記固定大綱例外；自測／認知科學校正清單；§9–§10 |
| **Source_rules** | 三子夾；連結；引讀五步；§6 同專題增量；G3/G4 |

## B8 同步規則

- 日常以磁碟 Canon + `skills/` 為準；本檔種子為重置快照
- 改 L1 → 同步 Skill + 本檔種子（kv-rules-sync）
- 漂移 → 列入落差，由用戶決定以哪側為準


