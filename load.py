import psycopg2
from psycopg2.extras import execute_values
from config import DB_CONFIG
from datetime import datetime

def upsert_data(df, table_name):
    """Upsert data into PostgreSQL and log the process in fredflow_logs."""
    print(f"\nUpserting data into PostgreSQL...")
    
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Start timestamp
    start_timestamp = datetime.now()
    
    # Prepare data for upsert
    columns = ["RELEASE_DATE", "DATA_VALUE", "RELEASE_JDN", "CAL_QUARTER_KEY", "FIRST_CREATED", "LAST_UPDATED"]
    values = [tuple(row) for row in df.to_numpy()]
    
    # Upsert query for main data table
    insert_query = f"""
    INSERT INTO {table_name} ({", ".join(columns)})
    VALUES %s
    ON CONFLICT (RELEASE_DATE) 
    DO UPDATE SET 
        DATA_VALUE = EXCLUDED.DATA_VALUE,
        LAST_UPDATED = EXCLUDED.LAST_UPDATED;
    """
    
    execute_values(cursor, insert_query, values)
    
    # Stop timestamp and row count
    stop_timestamp = datetime.now()
    row_tally = len(values)

    # Insert log into fredflow_logs table
    log_query = """
    INSERT INTO fredflow_logs (fred_series, row_tally, start_timestamp, stop_timestamp)
    VALUES (%s, %s, %s, %s);
    """
    
    cursor.execute(log_query, (table_name, row_tally, start_timestamp, stop_timestamp))
    
    # Commit and close connection
    conn.commit()
    cursor.close()
    conn.close()

    print(f"Successfully upserted {row_tally} rows into '{table_name}' and logged the process.")
