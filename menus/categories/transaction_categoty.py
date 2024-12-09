from db import get_db
from menus.categories.filtered_transactions import get_transactions_by_category


def get_all_categories():
    database = get_db()
    try:
        categories_list = database.execute(
            "SELECT DISTINCT category FROM transactions",
        )
        database.commit()
        return categories_list
    except Exception as e:
        print(f"failed to process your action, please try again => {e}")


def show_menu():
    [print(f"=> {categ_item[0]}") for categ_item in get_all_categories()]
    print("=> Exit")
    return input("\nwrite your choice: ")


def category_menu_switcher():
    continue_work = True
    user_choice = show_menu() or ""
    while continue_work:
        if user_choice.lower() == 'exit':
            continue_work = False
        else:
            result = get_transactions_by_category(user_choice)
            if result:
                user_choice = ""
                show_menu()
    if not continue_work:
        return True
