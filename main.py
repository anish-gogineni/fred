from extract import fetch_fred_data
from transform import transform_data
from load import upsert_data
from config import FRED_SERIES_MAPPING

def run_etl(series_id, table_name):
    """Run the full ETL process."""
    print(f"\nStarting ETL for {series_id} -> {table_name}")
    df = fetch_fred_data(series_id)
    transformed_df = transform_data(df)
    upsert_data(transformed_df, table_name)
    print(f"ETL completed for {series_id} -> {table_name}")

if __name__ == "__main__":
    for series_id, table_name in FRED_SERIES_MAPPING.items():
        run_etl(series_id, table_name)
