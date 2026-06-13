$ErrorActionPreference = "Stop"
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$BackendRoot = Join-Path $ProjectRoot "backend"
$FrontendRoot = Join-Path $ProjectRoot "frontend"
$VenvPython = Join-Path $BackendRoot ".venv\Scripts\python.exe"
$VenvPip = Join-Path $BackendRoot ".venv\Scripts\pip.exe"

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
Require-Command "node" "Install Node.js LTS from https://nodejs.org/ or run: winget install OpenJS.NodeJS.LTS"
Require-Command "npm" "npm comes with Node.js. Reopen PowerShell after installing Node."

Set-Location $BackendRoot
if (-not (Test-Path $VenvPython)) {
    python -m venv .venv
}
& $VenvPip install -r requirements.txt

Set-Location $FrontendRoot
npm install

$backendCommand = "cd `"$BackendRoot`"; .\.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"
$frontendCommand = "cd `"$FrontendRoot`"; npm run dev"

Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendCommand
Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendCommand

Write-Host "Backend starting at: http://localhost:8000" -ForegroundColor Green
Write-Host "Frontend starting at: http://localhost:3000" -ForegroundColor Green
Write-Host "Alpha v1 status: http://localhost:8000/api/alpha/v1/status" -ForegroundColor Green
