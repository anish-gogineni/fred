FRED_API_KEY = "your_fred_api_key"

DB_CONFIG = {
    "dbname": "your_db_name",
    "user": "your_username",
    "password": "your_password",
    "host": "your_db_host",
    "port": "5432",
}


# List of FRED series to be fetched
# Dictionary mapping FRED series to database table names
FRED_SERIES_MAPPING = {
    "GDP": "GDP",   # Gross Domestic Product
    "UNRATE": "UNRATE", # Unemployment Rate
    "DFF": "DFF",  # Effective Federal Funds Rate,
    "CPIENGSL": "CPIENGSL",  # Energy in US City Average
    "GFDEBTN": "GFDEBTN",  # Total Public Debt	
    "CORESTICKM159SFRBATL": "CORESTICKM159SFRBATL"  # Sticky CPI
}