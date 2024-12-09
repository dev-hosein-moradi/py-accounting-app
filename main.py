# create a menu for all section of app
# divide public and protected route
import sqlite3

from db import init_db
from menus.auth.auth_menu import register_form, login_form
from menus.categories.transaction_categoty import category_menu_switcher
from menus.profile.user_profile import get_user
from menus.reports.report import report_menu_switcher
from menus.transaction_manager.menu import menu_switcher


def app_menu():
    print("1- Register")
    print("2- Login")
    print("3- Profile")
    print("4- Transaction Management")
    print("5- Categorization")
    print("6- Reports")
    print("7- Exist")
    return input("choose your action: ")

def main():
    continue_work = True
    user_choice = ""
    user_choice = app_menu()
    while continue_work:
        if user_choice == "7":
            continue_work = False
        elif user_choice == "1":
            result = register_form()
            if result:
                user_choice = ""
                app_menu()
        elif user_choice == "2":
            result = login_form()
            if result:
                user_choice = ""
                app_menu()
        elif user_choice == "3":
            result = get_user()
            if result:
                user_choice = ""
                app_menu()
        elif user_choice == "4":
            result = menu_switcher()
            if result:
                user_choice = ""
                app_menu()
        elif user_choice == "5":
            result = category_menu_switcher()
            if result:
                user_choice = ""
                app_menu()
        elif user_choice == "6":
            result = report_menu_switcher()
            if result:
                user_choice = ""
                app_menu()
# call main app
main()