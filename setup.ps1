# AI-Powered AWS Smart Terminal - Setup Script
# Run this script in PowerShell to set up the project

Write-Host "🚀 AI-Powered AWS Smart Terminal Setup" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8 or higher." -ForegroundColor Red
    Write-Host "  Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Check pip
Write-Host ""
Write-Host "Checking pip..." -ForegroundColor Yellow
try {
    $pipVersion = pip --version 2>&1
    Write-Host "✓ Found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ pip not found!" -ForegroundColor Red
    exit 1
}

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Cyan
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dependencies installed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Create config.ini file if it doesn't exist
Write-Host ""
if (Test-Path "config.ini") {
    Write-Host "✓ config.ini file already exists" -ForegroundColor Green
} else {
    Write-Host "Creating config.ini file from template..." -ForegroundColor Yellow
    Copy-Item "config.ini.example" "config.ini"
    Write-Host "✓ config.ini file created" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠️  IMPORTANT: Edit config.ini file and add your credentials!" -ForegroundColor Yellow
    Write-Host "   - Set mode (demo/iam/root)" -ForegroundColor Cyan
    Write-Host "   - Add GEMINI_API_KEY" -ForegroundColor Cyan
    Write-Host "   - Configure AWS profiles using: aws configure --profile <name>" -ForegroundColor Cyan
}

# Summary
Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "✓ Setup Complete!" -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Edit config.ini file with your Gemini API key" -ForegroundColor White
Write-Host "2. Configure AWS credentials: aws configure --profile iam-user" -ForegroundColor White
Write-Host "3. Run: python main.py" -ForegroundColor White
Write-Host ""
Write-Host "For detailed instructions, see QUICKSTART_AWS_PROFILES.md" -ForegroundColor Cyan
Write-Host ""
