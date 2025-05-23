import pandas as pd
import sqlite3

def load_data(df: pd.DataFrame, db_path: str, table_name: str = "taxi_data"):
    print(f"\nLoading data into {db_path} ...")

    #Connect to SQLite DB(it will create the file if it doesn't exist)
    conn =  sqlite3.connect(db_path)

    #Load DataFrame into a SQL table (overwrite mode)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()
    print(f"Data loaded into table '{table_name}' successfully.")
    