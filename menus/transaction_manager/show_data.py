import pandas as pd

from db import get_db


def display_data():
    database = get_db()
    try:
        print("start read data from database...!")
        df = pd.read_sql("SELECT * FROM transactions", database)
        print(df)
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")