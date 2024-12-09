import pandas as pd

from db import get_db


def insert_transaction_data():
    database = get_db()

    try:
        df = pd.read_csv('data/transactions.csv')
        df.to_sql('transactions', database, if_exists='append', index=False)
        print("CSV data uploaded successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
        return False
    finally:
        database.close()