import pandas as pd

from db import get_db

def get_report(date):
    database = get_db()
    try:
        print("start read data from database...!")
        query = "SELECT * FROM transactions WHERE date LIKE ?"
        df = pd.read_sql(query, database, params=(f"{date}%",))
        print(df)
        return True
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
