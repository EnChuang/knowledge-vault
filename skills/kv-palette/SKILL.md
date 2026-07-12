---
name: kv-palette
description: >
  Knowledge Vault color palette lookup table — read/write Project/配色查詢表.md
  with duplicate detection before append. Use when adding palettes, querying colors
  for PPT/diagrams, or user says 配色查詢、新增配色、加入色板.
metadata:
  short-description: "KV palette — 配色查詢表去重寫入"
---

# kv-palette — 配色查詢表

Canon：`Project_rules.md` §13。唯一檔案：`Project/配色查詢表.md`。

## 定位

| 項目 | 規範 |
|------|------|
| 用途 | PPT、畫圖、UI 時查 palette；持續累積 |
| 格式 | 每組 8 色（C1–C8），ID 為 `P-###` |
| 去重 | **寫入前必查**；重複則**拒寫** |
| 例外 | **不需 MOC**、**不需讀者自測**（覆蓋 kv-project §3） |

**比喻**：配色查詢表像色票櫃——新色票入櫃前先對色號，已有同款就不重複掛牌。

## 觸發

- 用戶說：配色查詢、查配色、新增配色、加入色板、請寫入配色
- 貼入 HEX list 或 Console 輸出要求存入
- 做 PPT／圖表前請推薦或列出既有 palette

## 讀取（查詢）

1. 讀 `Project/配色查詢表.md` 主表
2. 依 `P-###` 或暱稱回覆 HEX 列
3. 未指定 ID → 可依色調（藍／綠／暖色／灰階）簡述候選

## 寫入前：去重（必跑）

### 1. 解析候選色

從用戶輸入抽出 **恰好 8 個** `#RRGGBB`（順序保留）。來源含：

- `HEX list: #xxx, #yyy, …`
- `console.table` 的 `hex` 欄
- 逗號／空白分隔的 8 色清單

不足或超過 8 色 → **拒寫**，請用戶補齊或裁切。

### 2. 計算簽章（palette-sig）

```
sig = lower(hex1) + "|" + lower(hex2) + … + lower(hex8)
```

- 僅比對 **6 位 hex**；`#` 可省略
- **大小寫不敏感**；**槽位順序敏感**（C1–C8 對調視為不同 palette）

### 3. 比對既有

```bash
grep "palette-sig\\|<!-- sigs" Project/配色查詢表.md
```

比對 `<!-- sigs` 區塊內 `P-###:hex1|…|hex8` 列，或舊版 `<!-- palette-sig: … -->`。

| 結果 | 行為 |
|------|------|
| sig 已存在 | **不寫入**；回報對應 `P-###` 與一鍵複製列 |
| sig 不存在 | 進入寫入 |

## 寫入（請寫入時）

1. **kv-method L-全** → **kv-flow** §3（本檔免 MOC／自測）
2. 取下一 ID：`P-` + 三位數（現有最大 +1；初建從 P-001）
3. 同次更新（保持簡潔，**僅一表 + sigs 區**）：
   - 主表新增一列：`| P-### | {暱稱} | \`#..., …\` |`
   - `<!-- sigs` 區塊末尾新增：`P-###:{sig}`
   - frontmatter `updated` 改當日
4. 不寫明細區、來源段、C1–C8 子表（除非用戶明確要求）
5. HEX 顯示：保留來源大小寫；sig 一律小寫
6. 暱稱：2–4 字；用戶有指定則用指定名
7. 寫入後簡報：新 ID、暱稱、是否曾拒絕重複項

## 禁止

- 未跑去重就追加
- 把規則正文寫進 `配色查詢表.md`（規則在 Skill + Canon）
- 拆成多檔或另建子 MOC（除非用戶明確要求重構）

## 與其他 Skill

| Skill | 關係 |
|-------|------|
| kv-project | 本檔豁免白皮書／自測；標籤仍用 `設計/配色` |
| kv-flow | 請寫入時走 §3 A + 本 Skill 去重 |
| kv-memory | 大量新增後可更新 MEMORY 指向 |
| kv-rename | 更名 `配色查詢表` 時全庫 grep |