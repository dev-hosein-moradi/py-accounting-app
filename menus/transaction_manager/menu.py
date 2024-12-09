from menus.transaction_manager.insert_data import insert_transaction_data
from menus.transaction_manager.show_data import display_data


def show_menu():
    print('1- upload cvs file')
    print('2- show transactions')
    print('3- exit')
    return input("choose your action: ")

def menu_switcher():
    continue_work = True
    user_choice = show_menu() or ""
    while continue_work:
        if user_choice == '1':
            result = insert_transaction_data()
            if result:
                user_choice = ""
                show_menu()
        elif user_choice == '2':
            display_data()
            user_choice = ""
        elif user_choice == '3':
            continue_work = False
    if not continue_work:
        return True