import sqlite3


def init_db():
    with open('schema.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect('accounting_db')
    cursor = db.cursor()
    try:
        cursor.executescript(sql_script)
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.commit()
        db.close()

def get_db():
    return sqlite3.connect('accounting_db')

