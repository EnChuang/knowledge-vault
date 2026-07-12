# Sync kv-link-scan package slice to 建庫開箱（one-shot helper）
$Vault = Split-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) -Parent
$Pkg = Join-Path $Vault "建庫開箱（打包用）\建庫開箱（打包用）"
Copy-Item -Force (Join-Path $Vault "AGENTS.md") (Join-Path $Pkg "AGENTS.md")
Copy-Item -Force (Join-Path $Vault "Bootstrap.md") (Join-Path $Pkg "Bootstrap.md")
Get-ChildItem (Join-Path $Vault "skills\kv-*") -Directory | ForEach-Object {
    $dest = Join-Path $Pkg "skills" $_.Name
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -Recurse -Force (Join-Path $_.FullName "*") $dest
}
Write-Host "Synced AGENTS, Bootstrap, skills/kv-* -> $Pkg"