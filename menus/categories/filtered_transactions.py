import pandas as pd

from db import get_db


def get_transactions_by_category(category):
    database = get_db()
    try:
        print("start read data from database...!")
        query = "SELECT * FROM transactions WHERE category = ?"
        df = pd.read_sql(query, database, params=(category,))
        print(df)
        return True
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
