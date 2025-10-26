import pandas as pd

def add_primary_key(df: pd.DataFrame, pkey_name: str) -> pd.DataFrame:
    """
    Extract only the 'actual.stationmeasurements' data from Buienradar JSON feed.

    Parameters
    ----------
    df: pd.DataFrame
        dataframe to add a primary key to
       
    pkey_name: str
        name to give to the new primary key column 
        
    Returns
    -------
    pd.DataFrame
        DataFrame containing the weather station measurements.
    """
    if pkey_name not in df:
        df[pkey_name] = df.index + 1
        print(f"Primary key column '{pkey_name}' added.")
        return df
    else:
        raise ValueError("This column name already exists")

def select_columns(df: pd.DataFrame, column_list: list[str]) -> pd.DataFrame:
    
    for name in column_list:
        if name not in df:
            raise ValueError(f"The column '{name}' is not in the dataframe.")
        
    print(f"Selected {len(column_list)} columns from the dataframe")    
        
    return df[column_list]