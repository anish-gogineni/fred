import pandas as pd
from datetime import datetime

def transform_data(df):
    """Transform data to fit PostgreSQL schema."""
    print("\nTransforming data to fit PostgreSQL schema...")
    df["RELEASE_JDN"] = df["RELEASE_DATE"].apply(lambda x: x.to_julian_date())
    df["CAL_QUARTER_KEY"] = df["RELEASE_DATE"].dt.to_period("Q").astype(str)
    df["FIRST_CREATED"] = datetime.now()
    df["LAST_UPDATED"] = datetime.now()
    print("Successfully transformed data.")

    return df[["RELEASE_DATE", "DATA_VALUE", "RELEASE_JDN", "CAL_QUARTER_KEY", "FIRST_CREATED", "LAST_UPDATED"]]
