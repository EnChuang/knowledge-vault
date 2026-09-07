---
name: kv-link-scan
description: Use when the user asks to scan, add, remove, prune, or audit Knowledge Vault wikilinks, including unlinked terms, excessive links, and broken Source image embeds.
metadata:
  short-description: "KV link scan — add gaps, prune weak, fix Source imgs"
---

# kv-link-scan — 超連結掃描（補／刪／修）

Canon：`Workflow_rules.md` §5。寫入疊加 **kv-link**、**kv-flow**、**kv-method** L-全。

## Overview

超連結掃描：補缺口、修剪弱／過密、修圖路徑。  
腳本在 `scripts/`。預設只報告，請寫入才改檔。
方針：全庫統一的只有定位（Overview）＋少數硬閘／步驟方向；其餘表述、舉例、臨場策略不制式化，容許容錯與自由發揮。設計型若要鎖風格，再個別補 Reference，不上升成全庫義務。

## Agent 使用步驟

1. 確認範圍（專題／全庫）與模式（scan／apply／prune）。
2. 跑對應腳本；先報告。
3. 用戶請寫入／直接套用 → 完整交付閘後改檔。

## §1 核心

| 原則 | 行為 |
|------|------|
| 預設 | **只出報告**，不改檔 |
| 寫入 | 用戶「請寫入」／明確「直接套用」→ L-全 → kv-flow §3 → 套用 → §4 |
| 詞彙 | 僅連**已存在**知識節點；不發明節點、不建佔位 `.md` |
| 密度 | 每句 ≤2–3 wikilink；同檔同目標勿洗版 |
| 範圍 | 預設 `Project/` 頂層專題筆記；**可排除**目錄（常見：`life update`） |

## §2 觸發

- 掃描連結／補連結／專有名詞超連結
- **刪超連結／修剪／過密去重**
- 全庫或指定專題的 wikilink 缺口與弱連結
- 寫入後抽查（可併用 kv-audit G2／G3）

## §3 詞彙表

依序合併、去重；**長名稱優先**：

1. `Project/{專題}/*.md` 檔名（去 `.md`）
2. `{專題} — MOC.md` 樹內 `[[wikilink]]`
3. MOC `aliases`
4. 高頻（寫作必連）：`AI Agent 工程`、`MEMORY`、`DailyChange`、`Architecture-Status`

**掃描自動補時跳過**（易誤傷通名）：裸詞 `MOC`、`Session`（仍可用手動／寫作規範連）。

**預設排除目錄**：`_DailyChange`、`scaffold`（巢狀參考）。用戶可再 `--exclude "life update"` 等。

不掃：`*_rules.md`、`MEMORY.md`、L0/L1、Skill 檔正文當掃描目標。

## §4 可連結區段（補連結白名單）

| 區段 | 說明 |
|------|------|
| 章首 | `> **銜接**`、章首表「前置／後續」 |
| 關係／索引 | `## 5 Relationship Diagram`、`## 14 Further Reading` |
| 延伸 | `## 延伸`、`## 延伸閱讀` |
| MOC | `## 專題簡介`（稀疏） |

**黑名單**（不批次插入）：原理敘事正文、code fence、已在 `[[…]]`／`` ` ``、同檔 `title` 自身。

表格儲存格：**可**連出處／章名；**禁止**用「整表當一段」做同目標去重。

## §5 比對規則（補）

| # | 規則 |
|---|------|
| R1 | 整詞出現且尚未連結 → 候選 |
| R2 | 優先同專題，再跨專題 |
| R3 | 最長匹配 |
| R4 | 同段已有 ≥2 個 → 該段不再加 |
| R5 | Source 用 piped／`![[Source/…]]`，不當知識節點掃 |

## §6 修剪規則（刪／降密度）

僅在請寫入／直接套用時執行；先報告建議再動檔（或用戶已授權整輪）。

| 動作 | 條件 | 作法 |
|------|------|------|
| 自連 | `[[本檔 title]]` | 還原純文字（有 `\|顯示` 則留顯示） |
| 同行重複 | 同一非表格行內同目標 ≥2 | 留首次，其餘還原文字 |
| 同檔過密 | 同目標全文 > **3** 次 | 優先**保留**銜接／延伸區；其餘還原 |
| 通名誤連 | 批次產生的裸 `[[MOC]]` 等 | 還原；「運動科學」等跨專題通名勿因二字詞自動連 |
| 保護 | `## 延伸`／`銜接` 列 | **禁止**用「一句 ≤3 連」砍掉導航列 |

**不做**：為降密度而拆掉延伸區多連導航；不刪「卡片未建仍可連」的刻意前瞻連結（除非用戶點名）。

## §7 修正常見斷鏈類型

| 類型 | 作法 |
|------|------|
| 圖檔僅檔名 | `![[Foo.png]]` 且檔在 `Source/Image/` → `![[Source/Image/Foo.png]]` |
| 專題別名 | 如 `[[Art of resilience]]` → `[[Art of resilience — MOC]]`（以 aliases／MOC 名為準） |
| Ebook | 知識節點寫法缺路徑 → 改 `[[Source/Ebook/….pdf\|顯示]]` |

修完建議跑 kv-audit **G2／G3** 抽查。

## §8 流程

```
指定範圍（全庫／專題／--exclude）
  → 建詞彙（§3）
  → 掃白名單：未連結報告（§4–§5）
  → 掃弱連結／過密／圖路徑（§6–§7）→ 修剪報告
  → 用戶請寫入或「直接套用」
  → L-全 → 先補（apply）→ 再修剪（prune）→ 必要時修圖路徑
  → 複掃報告 + kv-flow §4 簡報
```

## §9 報告格式

```markdown
## kv-link-scan 報告

- 範圍：…
- 排除：…
- 詞彙節點數：N
- 待補：M
- 待修剪：P（self / dup_line / over_repeat）
- 待修圖路徑：I

### 待補（同專題 · 白名單）
| 檔案 | 區段 | 建議連結 | 片段 |

### 待修剪
| 檔案 | 規則 | 目標 | 備註 |

### 跨專題（需確認）
| 檔案 | 建議連結 | 備註 |
```

## §10 請寫入套用

1. kv-method **L-全**（Blocked 則停）
2. kv-flow §3 A、A3
3. 腳本順序：`apply_unlinked.py` → `prune_links.py`（可加 `--fix-images`）
4. §4 簡報：補幾處、刪幾處、修幾圖；建議再 `scan_unlinked.py` 或 G2

與 **kv-rename**：更名用 rename；本 Skill 管**從未連**與**過密／弱連**。

## §11 輔助腳本

```bash
# 報告（預設排除 _DailyChange；可再排除專題夾）
python skills/kv-link-scan/scripts/scan_unlinked.py
python skills/kv-link-scan/scripts/scan_unlinked.py --topic "AI Agent 工程"
python skills/kv-link-scan/scripts/scan_unlinked.py --exclude "life update" --json

# 請寫入：補 → 修剪
python skills/kv-link-scan/scripts/apply_unlinked.py --exclude "life update"
python skills/kv-link-scan/scripts/prune_links.py --exclude "life update" --fix-images

# 改 skills/ 後鏡像
python skills/kv-link-scan/scripts/sync_package.py
```

## §12 與其他 Skill

| Skill | 關係 |
|-------|------|
| **kv-link** | 語法、高頻、兩類型 |
| **kv-audit** G2／G3 | 目標存在、Source 實體 |
| **kv-token** | 全庫可分批 `--topic` |
| **kv-rules-sync** | 改本 Skill 後 sync_package |

