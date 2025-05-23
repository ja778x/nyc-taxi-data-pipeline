import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print("\nStarting Transformation...")

    #Drop rows with missing essential values
    df = df.dropna(subset = ["tpep_pickup_datetime", "tpep_dropoff_datetime", "trip_distance", "fare_amount" ])

    #Filter out zero or negative fares or distances
    df = df[(df["trip_distance"] > 0) & (df ["fare_amount"] > 0)]

    #convert datetime columns
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

    #Rename columns for clarity
    df = df.rename(columns = {
        "tpep_pickup_datetime" : "pickup_datetime",
        "tpep_dropoff_datetime" : "dropoff_datetime"
    })

    print(f"Data cleaned. Remaining rows : {len(df)}")

    return df