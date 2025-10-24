# Ollama Quick Start Script
# This script helps you test if Ollama is set up correctly

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " Ollama Setup Verification" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check 1: Is Ollama installed?
Write-Host "[1/4] Checking if Ollama is installed..." -ForegroundColor Yellow
$ollamaVersion = ollama --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Ollama is installed: $ollamaVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Ollama is not installed" -ForegroundColor Red
    Write-Host "    Download from: https://ollama.ai/`n" -ForegroundColor Yellow
    exit 1
}

# Check 2: Is Ollama server running?
Write-Host "`n[2/4] Checking if Ollama server is running..." -ForegroundColor Yellow
$ollamaRunning = Test-NetConnection -ComputerName localhost -Port 11434 -WarningAction SilentlyContinue -ErrorAction SilentlyContinue
if ($ollamaRunning.TcpTestSucceeded) {
    Write-Host "✅ Ollama server is running on port 11434" -ForegroundColor Green
} else {
    Write-Host "❌ Ollama server is not running" -ForegroundColor Red
    Write-Host "    Start Ollama from the Start menu or restart your computer`n" -ForegroundColor Yellow
    exit 1
}

# Check 3: Are any models downloaded?
Write-Host "`n[3/4] Checking for downloaded models..." -ForegroundColor Yellow
$models = ollama list 2>$null
if ($models) {
    Write-Host "✅ Found models:" -ForegroundColor Green
    ollama list
    
    # Check if llama3.2 is available
    if ($models -match "llama3.2") {
        Write-Host "`n✅ llama3.2 is ready to use!" -ForegroundColor Green
        $modelReady = $true
    } else {
        Write-Host "`n⚠️  llama3.2 not found. Recommended model for this project." -ForegroundColor Yellow
        Write-Host "    Download it with: ollama pull llama3.2" -ForegroundColor Cyan
        $modelReady = $false
    }
} else {
    Write-Host "❌ No models found" -ForegroundColor Red
    Write-Host "    Download a model: ollama pull llama3.2`n" -ForegroundColor Yellow
    exit 1
}

# Check 4: Is .env configured?
Write-Host "`n[4/4] Checking .env configuration..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "✅ .env file exists" -ForegroundColor Green
    
    # Check if it's configured for Ollama
    $envContent = Get-Content ".env" -Raw
    if ($envContent -match "LLM_PROVIDER=ollama") {
        Write-Host "✅ Configured to use Ollama" -ForegroundColor Green
    } else {
        Write-Host "⚠️  .env exists but LLM_PROVIDER may not be set to 'ollama'" -ForegroundColor Yellow
        Write-Host "    Make sure your .env has: LLM_PROVIDER=ollama" -ForegroundColor Cyan
    }
} else {
    Write-Host "⚠️  .env file not found" -ForegroundColor Yellow
    Write-Host "    Copy .env.example to .env:" -ForegroundColor Cyan
    Write-Host "    Copy-Item .env.example .env`n" -ForegroundColor White
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " Setup Summary" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

if ($modelReady) {
    Write-Host "🎉 Everything looks good! You're ready to go!" -ForegroundColor Green
    Write-Host "`nNext steps:" -ForegroundColor Yellow
    Write-Host "  1. Make sure .env has: LLM_PROVIDER=ollama" -ForegroundColor White
    Write-Host "  2. Add a PDF to the data/ folder" -ForegroundColor White
    Write-Host "  3. Run: python src/chatbot.py`n" -ForegroundColor White
} else {
    Write-Host "⚠️  Almost there! Just download a model:" -ForegroundColor Yellow
    Write-Host "    ollama pull llama3.2`n" -ForegroundColor Cyan
}

Write-Host "========================================`n" -ForegroundColor Cyan
