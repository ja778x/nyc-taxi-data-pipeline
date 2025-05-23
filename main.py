import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pipeline.extract_data import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data

if __name__ == "__main__":
    filepath = (r"G:\DataProjects\nyc-taxi-data-pipeline\data\yellow_tripdata_2024-01.parquet")
    df_raw =  extract_data(filepath)
    print("\n Preview of raw data")
    print(df_raw.head())

    df_clean =  transform_data(df_raw)
    print("\nPreview of cleaned data: ")
    print(df_raw.head())

    db_path = "data/nyc_taxi.db"
    load_data(df_clean, db_path)