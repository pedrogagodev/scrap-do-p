import sys
import pandas as pd
from census_engine import CensusEngine

def main():
    if len(sys.argv) < 2:
        print("Usage: python search_cli.py \"<search_term>\"")
        print("Example: python search_cli.py \"poverty\"")
        sys.exit(1)

    search_term = sys.argv[1]
    
    try:
        # Initialize engine and load data
        engine = CensusEngine()
        df = engine.load_data()
        
        # Execute search
        results = engine.search(df, search_term)
        
        # Print summary
        count = len(results)
        print(f"\nFound {count} results for term: '{search_term}'\n")
        
        if count > 0:
            # Print Name and Label for terminal clarity
            # We use to_string to ensure all selected rows are shown without truncation
            print(results[['Name', 'Label']].to_string(index=False))
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
