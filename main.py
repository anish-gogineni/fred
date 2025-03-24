from extract import fetch_fred_data
from transform import transform_data
from load import upsert_data

def run_etl(series_id, table_name):
    """Run the full ETL process."""
    df = fetch_fred_data(series_id)
    transformed_df = transform_data(df)
    upsert_data(transformed_df, table_name)

if __name__ == "__main__":
    series_id = "GDP"  # Example metric
    table_name = "economic_data"
    run_etl(series_id, table_name)
