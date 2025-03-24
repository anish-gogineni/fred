FRED_API_KEY = "your_fred_api_key"

DB_CONFIG = {
    "dbname": "your_db_name",
    "user": "your_username",
    "password": "your_password",
    "host": "your_db_host",
    "port": "5432",
}


# Dictionary mapping FRED series to database table names
FRED_SERIES_MAPPING = {
    "GDP": "gdp",
    "UNRATE": "unemployment_rate",
}