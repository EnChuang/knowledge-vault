---
name: kv-memory
description: >
  Knowledge Vault cross-session memory — codec M2 read/write for AI-only MEMORY.md.
  Dictionary and L0-L3 retrieval here; MEMORY holds HOT+LOG data only. Use on resume,
  更新記憶, staged pause (ask before write), or after deliverables. DailyChange is human log.
metadata:
  short-description: "KV memory — M2 codec, MEMORY.md 第二大腦"
---

# kv-memory — 跨 Session 記憶（Codec M2）

> **人類用語**（見 [[Architecture-Status]]、[[AGENTS.md]]）：**輕量審查**＝L-輕；**完整交付審查**＝L-全；**機器交班格式**＝M2；**熱區**＝`[HOT]`；**歷史區**＝`[LOG]`。

Canon：庫根 `MEMORY.md` + `AGENTS.md` 記憶分工。人類日誌 → `Project/_DailyChange/DailyChange.md`。

## 分工

| 檔 | 讀者 | 內容 |
|----|------|------|
| `MEMORY.md` | **AI only** | `#M2` + `[HOT]` 快照 + `[LOG]` 無限追加 |
| 本 Skill | AI | 字典、讀寫協議、L0–L3 |
| `DailyChange.md` | 人（+AI 品管） | L-全 交付敘事、Verdict |

**禁止**：在 MEMORY 寫字典／中文說明；抄對話、L-全 全文、Project 正文。

---

## Codec M2 檔案格式

```text
#M2 u=YYMMDD s=vNN

[HOT]
act=...
pref=...
open=...
ptr=...

[LOG]
YYMMDD|kind|payload|ref
...
```

| 行 | 意義 |
|----|------|
| `#M2` | codec 版本；升級時改 Skill + 遷移腳本 |
| `u=` | 最後更新日 YYMMDD |
| `s=` | Bootstrap 種子短碼 `v18` = 2026-07-06-v18 |

### LOG 列：`YYMMDD|kind|payload|ref`

| kind | 用途 |
|------|------|
| `done` | 已完成任務（歸檔） |
| `pref` | 偏好演進（歷史保留；HOT 只留最新） |
| `act` | 進行中快照（通常只寫 HOT） |
| `open` | 待決策 |
| `ptr` | 新增常用指標 |
| `void` | 作廢：`void\|原日期\|原kind\|原payload` |
| `note` | 短註（非正文） |

`ref`：wikilink、`AGENTS:vNN`、`§12`、路徑短碼。`payload` 用 `+` 串事件、`,` 串並列鍵。

---

## 字典（payload／HOT 短碼）

### kind／結構

| 碼 | 義 |
|----|-----|
| `act=-` | 無進行中 |
| `open=-` | 無開放項 |
| `lfull>dc` | L-全 日誌寫 DailyChange |
| `pause>ask` | 階段收工須詢問才寫 MEMORY |

### 偏好 `pref`

| 碼 | 義 |
|----|-----|
| `ebook§12` | Ebook 蒸餾預設 [[Project_rules]] §12 |
| `fmt:$$+m+10q+ax` | 公式+符號註解+比喻；10 題；答案含解釋 |
| `ax` | 答案含解釋（answer+explain） |
| `m` | 比喻（metaphor） |

### 任務 payload 常見

| 碼 | 義 |
|----|-----|
| `spi` | 信號與電源完整性（Bogatin） |
| `mem` | MEMORY／記憶架構 |
| `kv-mem` | kv-memory Skill |
| `dc` / `dc-rename` | DailyChange |
| `palette` | 配色查詢表 |
| `kv-palette` | kv-palette Skill |
| `M2-codec` | MEMORY 改 M2 機器格式 |

### HOT `ptr` 短碼 → wikilink

| 碼 | 指向 |
|----|------|
| `s18` 等 | 種子版本（`s` + 數字 = v18） |
| `arch` | [[Architecture-Status]] |
| `dc` | [[DailyChange]] |
| `palette` | [[配色查詢表]] |

---

## 讀取 L0–L3（token 節制）

| 級 | 時機 | 動作 |
|----|------|------|
| **L0** | 一般任務 | 不讀 MEMORY |
| **L1** | 接續、冷啟動、寫入前 | 只讀 `#M2` + `[HOT]`（`Read` 限段或 grep `^\[HOT\]`） |
| **L2** | 「記得嗎／上次／某專題」 | `grep` `[LOG]` + 關鍵碼（`spi\|palette\|日期`） |
| **L3** | 明確全盤回顧 | 讀完整 `[LOG]`（罕見） |

夠用 MOC + 當次筆記 → 維持 L0。

---

## 階段性收工（必問，不自動寫）

觸發：「今天先這樣」「先告一段落」「收工」等。

> 要把這次進度蒸餾進 `MEMORY.md` 嗎？（說「要」或「請寫入」我才更新。）

| 回覆 | 行為 |
|------|------|
| 要／請寫入 | 依 §寫入更新 |
| 不要／未表態 | 不寫 |

---

## 寫入（請寫入）

1. 載入本 Skill → L1 讀 HOT
2. 若有新事實：`[LOG]` **末尾追加**（不改舊行）
3. **重算 HOT**（蒸餾，≤15 行）：
   - `act`：≤3 項，`專題碼→[[MOC]]` 或 `-`
   - `pref`：合併最新偏好，逗號串鍵
   - `open`：未關項或 `-`
   - `ptr`：`sNN,arch,dc,…` 常用指標
4. 更新 `#M2 u=`、`frontmatter updated`
5. 交付細節／Verdict → **DailyChange**（kv-method L-全），不寫進 LOG 長文

### LOG 追加範例

```text
260706|done|spi:13+§12|[[信號與電源完整性（Bogatin 簡化版） — MOC]]
260706|pref|ebook§12+ax|§12
260706|void|260605|done|old-task
```

### 禁止

- 未請寫入就改 MEMORY
- LOG 寫中文段落、12 節 QC、色碼清單全文
- 在 MEMORY 內嵌字典（字典只在本 Skill）

---

## 與其他 Skill

| Skill | 關係 |
|-------|------|
| kv-method | L-全 → DailyChange；MEMORY 只收交班蒸餾 |
| kv-token | 大 LOG 用 L2 grep，避免 L3 |
| kv-flow | 請寫入走 §3；MEMORY 免 MOC |
| kv-rename | 路徑／節點更名 → grep LOG + 更新 ptr |