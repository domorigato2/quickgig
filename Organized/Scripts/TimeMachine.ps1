# TimeMachine.ps1
Write-Host @"
=============================
    FSOCIETY TIME MACHINE
=============================
Initializing temporal core...
"@ -ForegroundColor Green
Start-Sleep -Seconds 2
$targetYear = Read-Host "Enter target year (e.g., 1985)"
Write-Host "Calibrating flux capacitor for $targetYear..." -ForegroundColor Cyan
Start-Sleep -Seconds 1
Write-Host "Scanning temporal anomalies: "
for ($i = 1; $i -le 5; $i++) {
    Write-Host "#" -NoNewline -ForegroundColor Red
    Start-Sleep -Milliseconds 500
}
Write-Host "`nScan complete. Engaging time warp!" -ForegroundColor Green
$testFile = "C:\Users\sheil\gig_delivery\temporal_log.txt"
if (-not (Test-Path $testFile)) {
    New-Item -Path $testFile -ItemType File | Out-Null
}
$newDate = (Get-Date).AddYears(- ( (Get-Date).Year - $targetYear ))
Set-ItemProperty -Path $testFile -Name LastWriteTime -Value $newDate
Write-Host "File timestamp altered to $targetYear!" -ForegroundColor Magenta
$log = "Time Travel Log: $(Get-Date)`nTarget Year: $targetYear`nStatus: Success`n"
Add-Content -Path $testFile -Value $log
Write-Host "Log saved to temporal_log.txt. Welcome to $targetYear, $(whoami)!" -ForegroundColor Green
Write-Host "Gig Hustler Mode Engaged!" -ForegroundColor Magenta
$gigTips = @("Gig landed! Check Fiverr bids.", "Portfolio poppin' at github.com/domorigato2/quickgig!", "Keep hustlin', coder!")
Write-Host "Gig Tip: $($gigTips | Get-Random)" -ForegroundColor Green
[Console]::Beep(900, 200); [Console]::Beep(1100, 200); [Console]::Beep(1300, 200)
Start-Sleep -Seconds 1