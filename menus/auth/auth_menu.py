from time import sleep

from pydantic import BaseModel, EmailStr, Field, ValidationError
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    username: str
    email: EmailStr
    password: str

def validate_user(**user_data):
    try:
        User(email=user_data['email'], username=user_data['username'], password=user_data['password'])
        return True
    except ValidationError as e:
        print(f"ERROR => {e}")
        return False

def get_user_data(title: str):
    print(f"welcome to {title} form")
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    return {
        "email": email,
        "username": username,
        "password": password
    }

def register_form():
    form = get_user_data("register")

    user_data = dict(email=form['email'], username=form['username'], password=form['password'])

    try:
        if validate_user(**user_data):
            db = get_db()
            user = db.execute(
                "SELECT * FROM user WHERE username = ?", (form['username'])
            ).fetchone()
            if user is None:
                db.execute(
                    "INSERT INTO user (email, username, password) VALUES (?, ?, ?)",
                    (form['email'], form['username'], generate_password_hash(form['password'])),
                )
                db.commit()
                print("user registered successfully!")
                sleep(2)
                return True
            else:
                print("user already exists!")
                return False
        else:
            print("failed to register user!")
    except Exception as e:
        print(f"failed to process your action, please try again => {e}")

def login_form():
    form = get_user_data("login")

    user_data =  dict(email=form['email'], username=form['username'], password=form['password'])
    try:
        if validate_user(**user_data):
            error = ""
            db = get_db()
            user = db.execute(
                "SELECT * FROM user WHERE username = ?", (form['username'],)
            ).fetchone()
            db.commit()
            if user is None:
                error = "user does not exist!"
            elif not check_password_hash(user["password"], form['password']):
                error = "invalid password!"

            if error == "":
                print("login successfully!")
                sleep(2)
                return True
            else:
                print(error)
                return False
        else:
            print("failed to logged in user!")
    except Exception as e:
        print(f"failed to process your action, please try again => {e}")