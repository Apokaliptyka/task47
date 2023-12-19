from change_data import change_user_data
from dell_data import deleted_user_data


def menu_user(login):
    while True:
        user_menu = input("""
        Меню користувача:
    
                        1.Зміна облікових даних
                        2.Видалення облікового запису
                        3.Повернутися на головну сторінку
        Введіть варінт: """)
        if user_menu=="1":
            change_user_data(login)
        if user_menu=="2":
            deleted_user_data(login)
            break
        if user_menu=="3":
            break



