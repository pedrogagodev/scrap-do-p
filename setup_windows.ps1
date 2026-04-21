# Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python is not installed or not in PATH." -ForegroundColor Red
    exit 1
}

Write-Host "--- Setting up Census Variable Searcher (Windows) ---" -ForegroundColor Cyan

# Create Virtual Environment
if (!(Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate and Install
Write-Host "Installing dependencies..."
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "To use the CLI, run: .\venv\Scripts\python.exe search_cli.py `"your_term`""
Write-Host "To use the Notebook, open it in VS Code or run 'jupyter notebook'."
