# src/extract.py
import requests
import pandas as pd

def extract_json_to_df(api_url: str, path: list[str]) -> pd.DataFrame:
    """
    Extract only the 'actual.stationmeasurements' data from Buienradar JSON feed.

    Parameters
    ----------
    api_url : str
        URL to the Buienradar API (e.g. https://data.buienradar.nl/2.0/feed/json/actual/stationmeasurements)

    Returns
    -------
    pd.DataFrame
        DataFrame containing the weather station measurements.
    """
    try:
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()
        data = requests.get(api_url).json()
    except Exception as e:
        raise RuntimeError(f"❌ Failed to fetch data from {api_url}: {e}")

    # ---- Only take 'actual' → 'stationmeasurements' ----
    try:
        for key in path:
            data = data[key]
        df = pd.DataFrame(data)
    except Exception as e:
        raise ValueError(f"⚠️ Could not extract 'actual.stationmeasurements': {e}")

    if df.empty:
        raise ValueError("⚠️ No station measurements found in the response")

    print(f"✅ Extracted {len(df)} station measurements from Buienradar")
    return df
