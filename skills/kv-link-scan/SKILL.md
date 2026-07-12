---
name: kv-link-scan
description: >
  Knowledge Vault wikilink gap scan — vocabulary from MOC/titles, find unlinked
  knowledge nodes in Project notes, report or apply (請寫入) per zone rules.
  Use when user asks 掃描連結、補 wikilink、專有名詞超連結、連結健檢、link scan.
metadata:
  short-description: "KV link scan — report gaps, apply on 請寫入"
---

# kv-link-scan — 專有名詞連結掃描

Canon：`Grok_rules.md` §5。寫入規範疊加 **kv-link**、**kv-project** §6、**kv-flow** §1。

## §1 核心

| 原則 | 行為 |
|------|------|
| 預設 | **只出報告**，不改檔 |
| 寫入 | 用戶「請寫入」→ kv-method L-全 → kv-flow §3 → 套用 → §4 |
| 詞彙 | 僅連**已存在**知識節點；不發明節點、不建佔位 `.md` |
| 密度 | 遵守每句 ≤2–3 wikilink（kv-flow） |

## §2 觸發

- 掃描連結／補連結／專有名詞超連結
- 全庫或指定專題的 wikilink 缺口
- 寫入後抽查（可併用 kv-audit G2）

## §3 詞彙表（節點清單）

依序合併、去重；**長名稱優先**（避免 `Python` 吃掉 `Python 直譯器`）：

1. `Project/{專題}/*.md` 的 **檔名**（去 `.md`）＝ `title` 節點名
2. 各 `{專題} — MOC.md` 樹狀圖內 `[[wikilink]]`（含別名節點）
3. MOC `aliases`（專題別名，如 `Agent Harness`）
4. **kv-link** 高頻節點：`Agent Harness`、`Session`、`MOC`、`Grok Build`

排除：`Project/_DailyChange/`、`*_rules.md`、`MEMORY.md`、L0/L1、Skill 檔。

可執行：`python skills/kv-link-scan/scripts/scan_unlinked.py`（見 §9）。

## §4 可連結區段（白名單）

僅在下列區段**建議或寫入** wikilink；其餘預設**跳過**：

| 區段 | 說明 |
|------|------|
| 章首 | `> **銜接**`、章首 metadata 表「前置／後續」欄 |
| 關係／索引 | `## 5 Relationship Diagram`、`## 14 Further Reading` |
| 銜接／延伸 | 開頭銜接、結尾「延伸閱讀」小節（[[Project_rules]] §6） |
| MOC | `## 專題簡介`（2–5 句內，稀疏連結） |

**黑名單**（不批次插入）：

- 原理敘事正文（§1–§4、§6–§13 敘事段）
- 程式碼／表格／Mermaid 區塊內
- 已包在 `[[…]]`、`![[…]]`、`` ` `` 內
- 同檔 `title` 自身（不自我連結）

**Python 手冊**（[[章節編排規範]]）：§5、§14 至少跨 2 部別；同章正文再提可不再連。

## §5 比對規則

| # | 規則 |
|---|------|
| R1 | 節點名**整詞**出現且尚未連結 → 候選 |
| R2 | 優先**同專題**節點，再跨專題（kv-link） |
| R3 | 一處候選只連**一個**最長匹配節點 |
| R4 | 同段已有 ≥2 個 wikilink → 該段不再加 |
| R5 | Source 用 piped link，**不**當知識節點掃描 |

## §6 掃描流程

```
用戶指定範圍（全庫／專題／單檔）
  → 建詞彙表（§3）
  → 讀 MOC 掌握邊界
  → 逐檔掃白名單區段（§4）
  → 產出報告（§7）
  →（可選）用戶請寫入 → 套用 + kv-flow §4
```

## §7 報告格式

```markdown
## kv-link-scan 報告

- 範圍：{專題或全庫}
- 詞彙節點數：N
- 候選總數：M

### 高優先（同專題 · 白名單區段）

| 檔案 | 區段 | 原文片段 | 建議連結 |

### 跨專題（需人工確認）

| 檔案 | 區段 | 建議連結 | 備註 |

### 略過（黑名單區段命中數）

- {檔名}：原理正文 K 處（未列出，避免洗版）
```

## §8 請寫入套用

1. kv-method **L-全**（Blocked 則停）
2. kv-flow §3 A（僅指定檔／段）、A3 高頻節點
3. 執行 `apply_unlinked.py`（白名單區段、每段 ≤2 連結）或手動改報告確認列
4. §4 簡報：改了幾檔、幾處；建議再跑 `scan_unlinked.py` 或 kv-audit G2

與 **kv-rename** 分工：更名後用 kv-rename 替換舊名；本 Skill 處理**從未連結**的已知節點。

## §9 輔助腳本

```bash
# 全庫報告（預設）
python skills/kv-link-scan/scripts/scan_unlinked.py

# 單專題
python skills/kv-link-scan/scripts/scan_unlinked.py --topic "Python 生態系知識圖譜"

# JSON（供後處理）
python skills/kv-link-scan/scripts/scan_unlinked.py --json

# 請寫入：套用白名單區段（每段 ≤2 連結）
python skills/kv-link-scan/scripts/apply_unlinked.py
python skills/kv-link-scan/scripts/apply_unlinked.py --topic "Agent Harness"
```

`scan_unlinked.py` 只產報告；`apply_unlinked.py` 改檔前須用戶請寫入 + §8。

## §10 與其他 Skill

| Skill | 關係 |
|-------|------|
| **kv-link** | 連結語法與高頻節點 |
| **kv-audit** G2 | 驗證 `[[節點]]` 目標存在 |
| **kv-token** | 全庫掃描前先估 token；大庫可 `--topic` 分批 |
| **kv-moc** | 樹節點須已存在才進詞彙表 |
| **kv-rules-sync** | 改 `skills/` 後跑 `scripts/sync_package.py`（→ `.grok/skills/` + 開箱包） |