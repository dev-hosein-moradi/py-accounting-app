from time import sleep

from db import get_db

def get_user():
    username = input('Enter your username: ')
    try:
        if username is not None:
            db = get_db()
            user = db.execute(
                "SELECT * FROM user WHERE username = ?", (username,)
            ).fetchone()
            db.commit()
            if user is not None:
                print(f"email: {user[1]}")
                print(f"username: {user[2]}")
                sleep(3)
                return True
            else:
                print("Username does not exist")
                return False
    except Exception as e:
        print(f"failed to process your action, please try again => {e}")