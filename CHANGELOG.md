# Changelog

本專案遵循 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，版本號遵循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

內部**種子代次**（寫在 `AGENTS.md`／`Bootstrap.md`）與 Git 標籤可並存，例如公開 `v1.0.0` 對應種子 `2026-07-06-v18`。

## [Unreleased]

### Added

- `docs/for-reader/`：導覽索引 + 01 開箱／02 一頁紙／03 指令範本（原根目錄 For Reader 遷入）

### Changed

- README 改為人話開篇：先講能得到什麼、解決什麼，再上手；長說明拆到 `docs/for-reader/`

### Fixed

### Removed

- 根目錄 `(For Reader) 01–03`（改由 `docs/for-reader/` 承載）

---

## [1.0.0] - 2026-07-12

### Added

- 可重現開箱包：AGENTS、Bootstrap、MEMORY 種子、14 包 `kv-*` Skill  
- For Reader 01–03（導覽、架構一頁紙、Agent 指令範本）  
- 空白 `DailyChange` 範本（給使用者自己的交付紀錄）  
- GitHub 導向 README、CHANGELOG、LICENSE、.gitignore  

### Notes

- 種子版本：**2026-07-06-v18**  
- 載具：Grok Build（庫根啟動）  

[Unreleased]: https://github.com/EnChuang/knowledge-vault/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/EnChuang/knowledge-vault/releases/tag/v1.0.0
