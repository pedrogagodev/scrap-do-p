# Census API Variables Searcher (2024 ACS)

This project automates the extraction and searching of variables from the United States Census API (ACS 1-Year 2024). Instead of using `CTRL + F` on a heavy web page with nearly 37,000 rows, this script loads the data into a Pandas DataFrame, enabling instant searches and programmatic manipulation.

## 🚀 How It Works

The project consists of a Jupyter Notebook (`census_search.ipynb`) that performs the following steps:

1.  **Data Synchronization (Caching):**
    *   Checks if the local `census_variables_2024.csv` file exists.
    *   **First run:** Downloads the HTML from `https://api.census.gov/data/2024/acs/acs1/variables.html`, extracts the main table, and saves it as a CSV.
    *   **Subsequent runs:** Loads the data directly from the local CSV, saving time and bandwidth.
2.  **Search Engine:**
    *   Filters variables by the `Label` field.
    *   The search is **case-insensitive** (handles uppercase and lowercase automatically).
    *   Displays the variable code (`Name`), description (`Label`), concept (`Concept`), and other metadata.

## 📋 Prerequisites

To run the notebook, you will need:
*   Python 3.10+
*   Pandas
*   Requests
*   lxml (for HTML processing)
*   Jupyter or VS Code with the Jupyter extension

## 🛠️ Installation

### Automated Setup (Recommended)

**Windows:**
```powershell
.\setup_windows.ps1
```

**Linux/macOS:**
```bash
chmod +x setup_linux.sh
./setup_linux.sh
```

### Manual Setup
1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it:
   - Windows: `.\venv\Scripts\activate`
   - Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## 🔍 How to Use

### Option 1: Jupyter Notebook (Interactive)
1. Open the `census_search.ipynb` file.
2. Run the import and data loading cells.
3. In the **Search Interface** cell, change the value of the `search_term` variable.
4. Execute the cell (Shift + Enter).

### Option 2: CLI - Command Line (Fast)
You can now run searches directly from your terminal using the modularized engine:
```powershell
python search_cli.py "poverty"
```
Or for specific terms:
```powershell
python search_cli.py "Total: Sex by Age"
```

## 📂 Project Structure

*   `census_engine.py`: Core logic (shared between Notebook and CLI).
*   `search_cli.py`: Command-line interface for quick searches.
*   `census_search.ipynb`: Interactive notebook for searching.
*   `census_variables_2024.csv`: Local data cache.
*   `requirements.txt`: Required libraries.
*   `README.md`: Documentation.
