import pandas as pd
from fredapi import Fred
from config import FRED_API_KEY

def fetch_fred_data(series_id):
    """Fetch data from FRED API using fredapi and return a pandas DataFrame."""
    print("\nFetching data from FRED API using fredapi and returning a pandas DataFrame.")
    fred = Fred(api_key=FRED_API_KEY)
    data = fred.get_series(series_id)
    
    # Convert series to DataFrame
    df = pd.DataFrame(data, columns=["DATA_VALUE"])
    df.index.name = "RELEASE_DATE"
    df.reset_index(inplace=True)
    print(f"{series_id} data fetched successfully.")
    return df
