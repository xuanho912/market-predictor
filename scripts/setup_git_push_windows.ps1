param(
    [string]$RepoUrl = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

function Require-Command($Name, $InstallHint) {
    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $command) {
        Write-Host "$Name is not installed or not on PATH." -ForegroundColor Yellow
        Write-Host $InstallHint
        exit 1
    }
    return $command
}

Require-Command "git" "Install Git with: winget install --id Git.Git -e"

Set-Location $ProjectRoot
Write-Host "Project: $ProjectRoot"

git init
git status
git add .

$hasHead = $true
git rev-parse --verify HEAD *> $null
if ($LASTEXITCODE -ne 0) {
    $hasHead = $false
}

if ($hasHead) {
    git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Host "No staged changes to commit."
    } else {
        git commit -m "Freeze alpha v1 bounce candidate and forward validation framework"
    }
} else {
    git commit -m "Freeze alpha v1 bounce candidate and forward validation framework"
}

git branch -M main

$existingRemote = ""
git remote get-url origin *> $null
if ($LASTEXITCODE -eq 0) {
    $existingRemote = git remote get-url origin
}

if (-not $existingRemote) {
    if (-not $RepoUrl) {
        $RepoUrl = Read-Host "Enter GitHub repo URL, e.g. https://github.com/YOUR_USER/market-predictor.git"
    }
    git remote add origin $RepoUrl
}

git push -u origin main
Write-Host "Pushed market-predictor to GitHub." -ForegroundColor Green
