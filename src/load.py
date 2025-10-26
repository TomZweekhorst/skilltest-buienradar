# src/load.py
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    """Return SQLAlchemy engine for SQLite"""
    sqlite_path = os.getenv("SQLITE_PATH", "data/weather.db")
    os.makedirs(os.path.dirname(sqlite_path), exist_ok=True)
    return create_engine(f"sqlite:///{sqlite_path}")

def load_df_to_sqlite(df: pd.DataFrame, table_name: str, pkey_name: str):
    """
    Load a DataFrame into an SQLite table.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to load into the database.
    table_name : str
        Name of the table to create/replace.
    pkey_name : str
        Name of the column that is chosen as the primary key
    """
    engine = get_engine()
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False, index_label=pkey_name)
    print(f"✅ Loaded {len(df)} records into table '{table_name}'")
