$ErrorActionPreference = "Stop"
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$BackendRoot = Join-Path $ProjectRoot "backend"
$VenvPython = Join-Path $BackendRoot ".venv\Scripts\python.exe"
$VenvPip = Join-Path $BackendRoot ".venv\Scripts\pip.exe"
$LogDir = Join-Path $ProjectRoot "outputs"
$LogFile = Join-Path $LogDir "forward_alpha_v1_tracker.log"

function Require-Command($Name, $InstallHint) {
    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $command) {
        Write-Host "$Name is not installed or not on PATH." -ForegroundColor Yellow
        Write-Host $InstallHint
        exit 1
    }
    return $command
}

Require-Command "python" "Install Python from https://www.python.org/downloads/ and enable Add to PATH."

Set-Location $ProjectRoot
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

if (-not (Test-Path $VenvPython)) {
    Set-Location $BackendRoot
    python -m venv .venv
    & $VenvPip install -r requirements.txt
    Set-Location $ProjectRoot
}

Write-Host "Running Alpha v1 forward-only tracker..."
& $VenvPython -m backend.app.services.validation.forward_alpha_tracker 2>&1 | Tee-Object -FilePath $LogFile -Append
Write-Host "Tracker log: $LogFile" -ForegroundColor Green
Write-Host "Signals CSV: $(Join-Path $ProjectRoot 'outputs\forward_alpha_v1_signals.csv')" -ForegroundColor Green
Write-Host "Report: $(Join-Path $ProjectRoot 'outputs\forward_alpha_v1_report.md')" -ForegroundColor Green
