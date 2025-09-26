# FileOrganizer.ps1
$sourceDir = "C:\Users\sheil\gig_delivery"
$logFile = "$sourceDir\FileOrganizer.log"

function Write-Log {
    param($Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp - $Message" | Out-File -FilePath $logFile -Append -Encoding UTF8
}

$folders = @{
    "PDFs" = @(".pdf")
    "Images" = @(".jpg", ".png", ".gif")
    "Docs" = @(".doc", ".docx", ".txt")
    "Code" = @(".py", ".ps1", ".js")
}

foreach ($folder in $folders.Keys) {
    $path = Join-Path $sourceDir $folder
    if (-not (Test-Path $path)) {
        New-Item -Path $path -ItemType Directory
        Write-Log "Created folder: $path"
    }
}

Get-ChildItem -Path $sourceDir -File | ForEach-Object {
    $file = $_
    if ($file.Name -notin @("FileOrganizer.ps1", "analyze_log.py")) {
        foreach ($folder in $folders.Keys) {
            if ($folders[$folder] -contains $file.Extension.ToLower()) {
                $dest = Join-Path $sourceDir $folder
                $destPath = Join-Path $dest $file.Name
                if (-not (Test-Path $destPath)) {
                    Move-Item -Path $file.FullName -Destination $dest
                    Write-Log "Moved $($file.Name) to $dest"
                } else {
                    Write-Log "Skipped $($file.Name) - already exists at $dest"
                }
            }
        }
    }
}

# Zip organized folders
$zipPath = "$sourceDir\organized_files_$(Get-Date -Format 'yyyyMMdd_HHmmss').zip"
Compress-Archive -Path .\Code,.\Docs,.\Images,.\PDFs -DestinationPath $zipPath -Force
Write-Log "Created zip: $zipPath"

Write-Log "File organization complete."