---
title: (For Reader) 架構一頁紙
tags:
  - 方法論/知識庫
  - 方法論/Bootstrap
  - 讀者/For Reader
created: 2026-06-28
updated: 2026-07-06
---

# (For Reader) 架構一頁紙

> 讀者速讀用。AI **常駐只讀 `AGENTS.md`**；其餘由 **kv-* Skill** 觸發載入。  
> 種子版本：**2026-07-06-v18**

---

## 1. 帶什麼進空資料夾

**最少 4 項：`AGENTS.md` + `Bootstrap.md` + `MEMORY.md` + `skills/`**（給 Agent，勿改名）

建議整夾複製（含 `(For Reader)*`、`README.md`），一秒起庫。

用 AI 建庫 → 開 **`(For Reader) 03 Agent 指令範本.md`** 複製貼上。

---

## 2. 建庫四步

```
① 空目錄 + 複製本開箱包（或 AGENTS + Bootstrap + MEMORY + skills/）
② 終端 cd 到庫根 → 執行 grok → 新對話
③ Agent 載入 kv-bootstrap → B0→B7（四 L1 Canon + 複製 skills → .grok/skills/）
④ 貼 03 指令 ②，開第一個專題
```

**注意**：步驟 ③ 只需把 `skills/` 複製到 **`{庫根}/.grok/skills/`**；**不要求** `C:\Users\…\.grok\skills\` 有 kv-*。

---

## 3. 架構一圖

```text
AGENTS.md ───── L0（AI 自動讀，~120 行）
    │
    ├── kv-* Skill（依任務觸發，14 包）
    │     母本：skills/kv-*/
    │     執行：.grok/skills/kv-*/  ← Grok 在庫根啟動時發現
    │
    ├── *_rules.md ─ Canon 全文（Skill 要求時才讀）
    └── Bootstrap.md ─ 建庫種子（僅 kv-bootstrap）

MEMORY.md  僅 AI 交班（kv-memory；非常駐）
Project/   筆記 · Project/_DailyChange/DailyChange.md（完整交付審查單檔）
Source/    原文
README.md  人類使用說明
```

---

## 4. 記憶三分流

```text
對話結束 ──蒸餾──► MEMORY.md（AI 交班：熱區 + 歷史）
              │
              └──完整交付審查──► DailyChange（你看：最新一輪）
專題研究 ────────────────► Project/ 筆記 + MOC
```

| 白話 | Skill 內碼 | 意思 |
|------|------------|------|
| 輕量審查 | L-輕 | 討論、草稿 |
| 完整交付審查 | L-全 | 「請寫入」等重大交付 → DailyChange |
| 機器交班格式 | M2 | 僅 MEMORY.md 的壓縮寫法 |

---

## 5. Harness 四層（對照）

| 層 | 一句話 | 本庫檔案 |
|----|--------|----------|
| AGENTS | 去找誰 | `AGENTS.md` |
| Skill | 怎麼做 | `skills/` + `.grok/skills/` |
| MCP / 工具 | 有手腳 | Grok 讀檔、終端、可選 MCP |
| Hook | 自動發生 | 請寫入前完整交付審查、§3/§4（多為 Skill 軟約束） |

---

## 6. 職責一句話

| 層 | 職責 |
|----|------|
| AGENTS | 索引、Skill 註冊、任務→Skill 表 |
| kv-* Skill | **執行**規則（庫內 `.grok/skills/` 發現） |
| *_rules.md | **Canon**（人讀、健檢對照、wikilink） |
| Bootstrap | 空庫重置種子 |
| MEMORY | 僅 AI 跨 Session 交班 |

**優先序**：你的指令 ＞ 專項 Skill／Canon ＞ AGENTS。

---

## 7. Skill 路徑速查

| 路徑 | 用途 |
|------|------|
| `skills/kv-*/` | 母本；改 Skill 先改這裡 |
| `.grok/skills/kv-*/` | 執行鏡像；Grok 在庫根 cwd 時讀這裡 |
| `~/.grok/skills/` | Grok 全域內建（help、docx…）；**不含** kv-* 也正常 |
| `建庫開箱…/skills/` | 打包給他人的副本（G9 對齊） |

改母本後（完整庫維護者）：`python skills/kv-link-scan/scripts/sync_package.py`

---

## 8. 五條鐵律

1. 未說「請寫入」→ 只草稿  
2. 規範只寫 L0 / Skill / Canon  
3. 改 Canon → 同步 Skill + `Bootstrap.md` 種子  
4. 改 `skills/` → 跑 `sync_package.py`（→ `.grok/skills/` + 開箱包）  
5. **打包本夾前** → kv-audit G1–G10（含 G9）

---

## 9. 開箱包 vs 完整庫

| | 本夾開箱 | 完整 Knowledge Vault |
|--|----------|----------------------|
| 功能 | 齊 | 齊 |
| AGENTS | 精簡 L0 | 同左 |
| 條文 | Canon 種子 + Skill | Canon 較詳 + Skill |
| `.grok/skills/` | 建庫後由 Bootstrap 產生 | 通常已存在 |
| 用途 | 複製起點 | 日常實戰 + 打包源 |

---

## 10. 新安裝檢查清單

- [ ] `cd` 到含 `AGENTS.md` 的庫根  
- [ ] `grok` 從庫根啟動（非從隨機資料夾）  
- [ ] `.grok/skills/` 有 **14 包** kv-*  
- [ ] 四 L1 `*_rules.md` + `MEMORY.md` 存在  
- [ ] 貼 **03 指令 ⑧** 請 AI 確認任務→Skill 對照  

詳細流程 → **`(For Reader) 01 開箱導覽.md`**