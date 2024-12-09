from menus.reports.filtered_report import get_report


def show_menu():
    print('=> enter date e.g: 2023-01-01')
    print('=> exit')
    return input("enter date: ")

def report_menu_switcher():
    continue_work = True
    user_choice = show_menu() or ""
    while continue_work:
        if user_choice.lower() == 'exit':
            continue_work = False
        else:
            result = get_report(user_choice)
            if result:
                user_choice = ""
                show_menu()
    if not continue_work:
        return True