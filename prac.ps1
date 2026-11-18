
param(
    [Parameter(Position=0)]
    [string]$Action = "help",

    [Parameter(Position=1)]
    [string]$Target = ""
)

$Owner = "Adesh-so"
$Repo = "prac"
$Branch = "main"

$Api = "https://api.github.com/repos/$Owner/$Repo"
$Raw = "https://raw.githubusercontent.com/$Owner/$Repo/$Branch"

$Headers = @{
    "User-Agent" = "Prac-Downloader"
    "Accept" = "application/vnd.github+json"
}

function Get-Tree {
    $result = Invoke-RestMethod `
        -Uri "$Api/git/trees/$Branch`?recursive=1" `
        -Headers $Headers

    return $result.tree
}

function Download-One {
    param([string]$Path)

    $encoded = (($Path -split "/") | ForEach-Object {
        [uri]::EscapeDataString($_)
    }) -join "/"

    $destination = Join-Path (Get-Location) ($Path -replace "/", "\")
    $parent = Split-Path $destination -Parent

    if (!(Test-Path $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    Invoke-WebRequest -Uri "$Raw/$encoded" `
        -OutFile $destination

    Write-Host "Downloaded: $Path" -ForegroundColor Green
}

try {
    switch ($Action.ToLower()) {

        "get" {
            Invoke-WebRequest `
                -Uri "$Owner" `
                -ErrorAction SilentlyContinue | Out-Null

            $zip = Join-Path (Get-Location) "prac.zip"

            Invoke-WebRequest `
                -Uri "https://github.com/$Owner/$Repo/archive/refs/heads/$Branch.zip" `
                -OutFile $zip

            Expand-Archive -Path $zip `
                -DestinationPath (Get-Location) -Force

            Write-Host "Repository downloaded successfully!" -ForegroundColor Green
        }

        "list" {
            $tree = Get-Tree

            $files = $tree | Where-Object {
                $_.type -eq "blob" -and
                (
                    $Target -eq "" -or
                    $_.path.StartsWith($Target.TrimEnd("/") + "/")
                )
            }

            if ($files) {
                $files | ForEach-Object { Write-Host $_.path }
            }
            else {
                Write-Host "No matching files found."
            }
        }

        "download" {
            if ($Target -eq "") {
                $Target = Read-Host "Enter complete file path"
            }

            $tree = Get-Tree
            $match = $tree | Where-Object {
                $_.type -eq "blob" -and $_.path -eq $Target
            }

            if ($match) {
                Download-One $Target
            }
            else {
                Write-Host "File not found: $Target" -ForegroundColor Red
            }
        }

        "folder" {
            if ($Target -eq "") {
                $Target = Read-Host "Enter folder name"
            }

            $tree = Get-Tree
            $files = $tree | Where-Object {
                $_.type -eq "blob" -and
                $_.path.StartsWith($Target.TrimEnd("/") + "/")
            }

            if (!$files) {
                Write-Host "Folder not found or empty."
            }
            else {
                foreach ($file in $files) {
                    Download-One $file.path
                }

                Write-Host "Folder download completed!" -ForegroundColor Green
            }
        }

        default {
            Write-Host "PRACTICAL DOWNLOADER"
            Write-Host "prac get"
            Write-Host "prac list"
            Write-Host "prac list DSBDA"
            Write-Host "prac download"
            Write-Host "prac folder DSBDA"
        }
    }
}
catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}
