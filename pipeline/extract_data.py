import pandas as pd

def extract_data(filepath):
    print(f"Reading data from {filepath}")
    df = pd.read_parquet(filepath)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    return df