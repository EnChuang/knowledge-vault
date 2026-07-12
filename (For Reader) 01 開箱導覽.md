---
title: (For Reader) 開箱導覽
tags:
  - 方法論/知識庫
  - 方法論/Bootstrap
  - 讀者/For Reader
created: 2026-06-28
updated: 2026-07-06
---

# (For Reader) 開箱導覽

> 給**完全沒建過知識庫**的人。本資料夾名 **`建庫開箱（打包用）`**＝複製給他人建庫用。  
> **`AGENTS.md`**＝AI 自動讀（L0 索引）；**`Bootstrap.md`**＝建庫種子（不常駐）。種子版本：**2026-07-06-v18**。

---

## 本夾檔案分工

| 檔案 | 讀者 | 必備？ | 用途 |
|------|------|--------|------|
| **`AGENTS.md`** | AI | ✅ | L0 索引 + Skill 註冊表（常駐載入） |
| **`Bootstrap.md`** | AI（建庫時） | ✅ | B0–B7 種子；**不**塞進 AGENTS 以省 token |
| **`MEMORY.md`** | 僅 AI | ✅ | 跨對話交班（機器格式；你不必讀） |
| **`skills/kv-*/SKILL.md`** | AI（觸發） | ✅ | **14 包**執行規則（**母本**） |
| **`README.md`** | 你 | 建議 | 使用說明、術語對照、專題一覽 |
| **`(For Reader) 01–03`** | 你 | 建議 | 導覽、架構、指令範本 |

**帶走建庫**：複製整夾，或至少 `AGENTS.md` + `Bootstrap.md` + `skills/` + `MEMORY.md`。

---

## 記憶三分流（讀者版）

```text
對話結束 ──蒸餾──► MEMORY.md（僅 AI 交班：熱區 + 歷史）
              │
              └──完整交付審查──► DailyChange（你看：最新一輪改了什麼）
專題研究 ────────────────► Project/ 筆記 + MOC（正文權威）
```

| 檔 | 給誰 | 記什麼 |
|----|------|--------|
| `Project/` | 你 + AI | 專題怎麼寫 |
| `DailyChange.md` | **你為主** | 重大交付 Pass 與否 |
| `MEMORY.md` | **僅 AI** | 跨對話交班 |

---

## 建議閱讀順序

```
1. 本檔（操作流程 + Skill 路徑）
2. (For Reader) 02 架構一頁紙
3. (For Reader) 03 → 複製指令給 AI
```

---

## 新安裝：你是哪一種？

| 情境 | 你手上有什麼 | 要做什麼 |
|------|--------------|----------|
| **A. 收到本開箱包** | `AGENTS` + `Bootstrap` + `skills/`，可能還沒有 `.grok/skills/` | 貼 **03 指令 ①** 建庫；或見下方「人工建庫」 |
| **B. 收到完整 Knowledge Vault** | 整庫含 `.grok/skills/kv-*` | `cd` 庫根 → 執行 `grok`；**不必**再裝 Skill |
| **C. 全新電腦** | 已安裝 Grok，資料夾照 A 或 B | 同 A 或 B；**不必**事先在個人目錄放 kv-* |

**關鍵**：在**庫根**（含 `AGENTS.md` 的資料夾）啟動 `grok`。工作目錄必須是庫根，AI 才會讀到 L0 與庫內 Skill。

---

## Skill 放哪裡？（讀者必讀）

知識庫的 **kv-*** 跟著**資料夾**走，不跟著 Windows 使用者帳號走。

| 路徑 | 誰的 | kv-* 要在這嗎？ |
|------|------|-----------------|
| **`{庫根}/skills/`** | 知識庫 | ✅ **母本**（打包、版控、給別人的源） |
| **`{庫根}/.grok/skills/`** | 知識庫 | ✅ **必須**（Grok 在庫根啟動時自動發現） |
| **`C:\Users\你\.grok\skills\`** | 本機 Grok 全域 | ❌ **不必**（這裡是 help、docx 等內建 Skill） |

```text
收到開箱包
  skills/kv-*/          ← 母本（一定有）
       ↓ 建庫時複製
  {庫根}/.grok/skills/kv-*/   ← Grok 執行時讀這裡

C:\Users\你\.grok\skills\     ← 沒有 kv-* 是正常的
```

**常見誤解**：新電腦的 `C:\Users\????\.grok\skills\` 一開始沒有 kv-* **沒問題**；只要在**庫根**建好 `.grok/skills/` 即可。

**維護者**（完整庫改過 `skills/` 後）：在庫根執行  
`python skills/kv-link-scan/scripts/sync_package.py`  
→ 同步到庫內 `.grok/skills/` + 本開箱包（見 **03 指令 ⑧**）。

---

## Harness 四層（讀者版）

| 概念 | 一句話 | 本庫對應 |
|------|--------|----------|
| **AGENTS** | 告訴 AI「去找誰」 | `AGENTS.md`：任務 → kv-* 表 |
| **Skill** | 告訴 AI「怎麼做」 | `skills/kv-*/SKILL.md` |
| **MCP** | 讓 AI「有工具可以做」 | Grok 內建讀檔／終端；可另接 Notion 等 |
| **Hook** | 特定時機自動發生 | 多數靠 Skill 約束（如請寫入前完整交付審查）；非 Grok 硬 Hook |

日常：**AGENTS 常駐** → 依任務載入 **kv-* Skill** → 需要時才讀 **`*_rules.md` Canon**。

---

## 五分鐘建庫（AI 版，推薦）

1. 把本夾複製到你要當「庫根」的空資料夾
2. 終端機 `cd` 到該庫根
3. 執行 `grok`，開**新對話**
4. 貼 **`(For Reader) 03`** 指令 ①

Agent 會載入 **kv-bootstrap**，讀 `Bootstrap.md`，建立目錄與四 L1 Canon，並把 `skills/` 複製到 `.grok/skills/`。

### 建庫後請確認

- [ ] `{庫根}/.grok/skills/` 下有 **14 個** `kv-*/SKILL.md`（含 kv-memory、kv-palette）
- [ ] 庫根有四 L1 + `MEMORY.md` + `Project/_DailyChange/DailyChange.md`（DailyChange 單檔）
- [ ] 種子版本 **2026-07-06-v18**
- [ ] 在庫根執行 `grok` 後，可貼 **03 指令 ⑧** 驗證 Skill 可發現

（`~/.grok/skills/` 有無 kv-* **不影響**上述檢查。）

---

## 人工建庫（備用）

在**庫根**執行（PowerShell 範例）：

```powershell
# 1. 建 B1 骨架（見 Bootstrap.md；或請 AI 依 B1 建立）

# 2. 複製 Skill 母本 → 庫內執行目錄（必做）
New-Item -ItemType Directory -Force -Path .grok\skills
Copy-Item -Recurse skills\kv-* .grok\skills\

# 3. 建四 L1（Bootstrap B3–B6 種子，或從完整庫複製 Canon）

# 4. 庫根啟動 grok，跑 B7 驗收
```

---

## 給別人使用前（打包者）

1. 在完整庫跑 **kv-audit G9**（開箱包與庫根對齊）
2. 或執行 `python skills/kv-link-scan/scripts/sync_package.py`
3. 再複製整個 **`建庫開箱（打包用）`** 資料夾給對方
4. 告訴對方：讀 **本檔** → **02** → 貼 **03 指令 ①**；**不必**改對方電腦的 `C:\Users\…\.grok\skills\`

---

## 常見問題

**Q：還需要 `*_rules.md` 嗎？**  
A：要。Canon 供人讀、wikilink、健檢對照；日常執行靠 Skill，不必每次讀 Canon 全文。

**Q：Skill 放哪？Grok 怎麼找到？**  
A：母本在 `{庫根}/skills/`；執行鏡像在 `{庫根}/.grok/skills/`。在庫根啟動 `grok` 即自動發現。另見上方「Skill 放哪裡？」。

**Q：要複製到 `C:\Users\我\.grok\skills\` 嗎？**  
A：**不必**。那是 Grok 全域目錄；kv-* 應只在知識庫資料夾內。僅當你堅持「不在庫根開 grok 也要用到 kv-*」時才可選複製（不建議）。

**Q：新 Session 會自動用哪個 Skill？**  
A：Grok 掃描庫內 `.grok/skills/` + 全域內建；**知識庫任務**由 `AGENTS.md` 任務表決定載入哪些 kv-*。你不必每次手動指定路徑。

**Q：完整庫改規則後本夾要更新嗎？**  
A：要。跑 kv-audit **G9** 或 `sync_package.py` 對齊本夾後再打包給他人。

**Q：`MEMORY.md` 我要讀嗎？**  
A：**不必**。那是給 AI 的交班簿；你看 `DailyChange.md` 與 `Project/` 筆記即可。

---

## 下一步

- 貼指令 → `(For Reader) 03 Agent 指令範本.md`
- 速讀架構 → `(For Reader) 02 架構一頁紙.md`
- 使用說明 → `README.md`