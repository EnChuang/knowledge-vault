---
name: kv-rules-sync
description: >
  Knowledge Vault L0/L1/Skill/Bootstrap sync — cross-reference grep, seed updates,
  建庫開箱 alignment. Use when writing or changing rules, AGENTS.md, skills, or Bootstrap.md.
metadata:
  short-description: "KV rules sync — L0/L1/Skill/seed"
---

# kv-rules-sync — 規則同步

## 原則

規範定案 → 寫 **Canon**（對應 `*_rules.md`）+ 同步 **Skill** + **`Bootstrap.md` 種子** + **`AGENTS.md` 索引**（若職責變）。

日常真相：磁碟 Canon + `skills/`。Bootstrap 種子為重置快照。

## L0/L1 對照（新增／更名必跑）

| 觸發 | L0 必查 | 全部必查 |
|------|---------|----------|
| 新增條文 | AGENTS 任務表、Skill 表 | 目標 Canon；grep 其餘 L1+skills |
| 新建 L1 | 啟動前置、分類軸 | 讀四 Canon + 查 Skill 重複 |
| 更名 | AGENTS、Bootstrap、For Reader | grep 舊名於 L0+四L1+skills |
| 架構定案 | — | 同步 `建庫開箱（打包用）/`（G9） |

## 寫入規則檢查（kv-flow §3 D）

D1 層級（L0 只索引）· D2 歸檔 · D3 落差清單 · D4 AGENTS · D5 Bootstrap 種子 · D6 grep 四L1+L0+skills

## 寫入後（§4 C）

C1 落差回報 · C2 未擅自改歷史筆記 · C3 交叉引用 · C4 Bootstrap · C5 L0/L1 對照

## 健檢級別

- **小改**：grep L0+四L1+skills；更新對應 Bootstrap 種子
- **結構改**：讀全部 Canon+AGENTS+skills；更新任務表與開箱包

## Skill 鏡像同步（改 `skills/` 或 L0 涉架構後必跑）

磁碟真相源：`skills/kv-*/`（打包用母本）。**不會**自動複製；須執行：

```bash
python skills/kv-link-scan/scripts/sync_package.py
```

| 目標 | 用途 |
|------|------|
| `.grok/skills/` | Grok 庫內自動發現（**日常執行**） |
| `建庫開箱（打包用）/建庫開箱（打包用）/` | G9 開箱包（AGENTS、Bootstrap、skills、Review 種子） |

**不會**同步到 `~/.grok/skills/`（全域內建 Skill；勿覆寫 docx、help 等）。

改 Canon 且 Skill 摘要需對齊 → 先改 `skills/kv-*/SKILL.md`，再跑上列腳本。打包前另跑 **kv-audit** G9。