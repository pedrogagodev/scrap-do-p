import pandas as pd
import os
import requests

class CensusEngine:
    """
    Core logic for downloading, caching, and searching US Census API variables.
    """
    DEFAULT_URL = 'https://api.census.gov/data/2024/acs/acs1/variables.html'
    DEFAULT_CACHE = 'census_variables_2024.csv'

    @staticmethod
    def load_data(url=DEFAULT_URL, cache_file=DEFAULT_CACHE, force_download=False):
        """
        Loads data from local CSV if it exists, otherwise downloads from URL.
        """
        if not os.path.exists(cache_file) or force_download:
            print(f"Downloading data from {url}...")
            try:
                # Use pandas read_html with a match pattern to find the correct table
                tables = pd.read_html(url, match='Name')
                df = tables[0]
                
                # Cache the results
                df.to_csv(cache_file, index=False)
                print(f"Data cached successfully to {cache_file}")
                return df
            except Exception as e:
                raise Exception(f"Failed to download/parse data: {e}")
        else:
            # Load from cache
            return pd.read_csv(cache_file)

    @staticmethod
    def search(df, term):
        """
        Performs a case-insensitive search on the 'Label' column.
        """
        if 'Label' not in df.columns:
            return pd.DataFrame()
            
        term_lower = str(term).lower()
        # Fill NaN to avoid errors during string operations
        mask = df['Label'].fillna('').str.lower().str.contains(term_lower, regex=False)
        return df[mask]
