#!/bin/bash

# Check for Python
if ! command -v python3 &> /dev/null
then
    echo "Error: Python3 could not be found. Please install it."
    exit 1
fi

echo "--- Setting up Census Variable Searcher (Linux/macOS) ---"

# Create Virtual Environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate and Install
echo "Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo -e "\nSetup complete!"
echo "To use the CLI, run: ./venv/bin/python search_cli.py \"your_term\""
echo "To use the Notebook, open it in VS Code or run 'jupyter notebook'."
