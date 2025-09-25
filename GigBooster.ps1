# GigBooster.ps1
Write-Host "fsociety Gig Booster v1.0" -ForegroundColor Green
$clientName = Read-Host "Enter client name"
$gigType = Read-Host "Enter gig type (e.g., Time Machine, File Organizer)"
$proposal = "Hello $clientName,`nI'm a *Mr. Robot*-inspired coder building $gigType scripts in PowerShell. Check my portfolio: github.com/domorigato2/quickgig. Fast delivery, starting at $15!`nCheers,`nSheil"
Write-Host "Proposal Draft:`n$proposal" -ForegroundColor Cyan
$proposal | Out-File -FilePath "proposal_$clientName.txt"
Write-Host "Proposal saved to proposal_$clientName.txt" -ForegroundColor Green
[Console]::Beep(800, 200); [Console]::Beep(1000, 200)