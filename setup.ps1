
$ErrorActionPreference = "Stop"

$InstallDir = Join-Path $env:LOCALAPPDATA "prac"

New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

$DownloadUrl = "https://raw.githubusercontent.com/Adesh-so/prac/main/prac.ps1"

Invoke-WebRequest -Uri $DownloadUrl `
    -OutFile (Join-Path $InstallDir "prac.ps1")

$ProfileDir = Split-Path $PROFILE -Parent

if (!(Test-Path $ProfileDir)) {
    New-Item -ItemType Directory -Path $ProfileDir -Force | Out-Null
}

if (!(Test-Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force | Out-Null
}

$Marker = "# PRAC DOWNLOADER"

$Existing = Get-Content $PROFILE -Raw

if (!$Existing.Contains($Marker)) {
    Add-Content -Path $PROFILE -Value @'

# PRAC DOWNLOADER
function prac {
    & "$env:LOCALAPPDATA\prac\prac.ps1" @args
}
'@
}

. $PROFILE

Write-Host "Prac Downloader installed successfully!" -ForegroundColor Green
Write-Host "Try: prac list"
