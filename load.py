import psycopg2
from psycopg2.extras import execute_values
from config import DB_CONFIG

def upsert_data(df, table_name):
    """Upsert data into PostgreSQL."""
    print(f"\nUpserting data into PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    columns = ["RELEASE_DATE", "DATA_VALUE", "RELEASE_JDN", "CAL_QUARTER_KEY", "FIRST_CREATED", "LAST_UPDATED"]
    values = [tuple(row) for row in df.to_numpy()]
    
    insert_query = f"""
    INSERT INTO {table_name} ({", ".join(columns)})
    VALUES %s
    ON CONFLICT (RELEASE_DATE) 
    DO UPDATE SET 
        DATA_VALUE = EXCLUDED.DATA_VALUE,
        LAST_UPDATED = EXCLUDED.LAST_UPDATED;
    """
    
    execute_values(cursor, insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()

    print(f"Succesfully upserted data into PostgreSQL '{table_name}' Table.")
