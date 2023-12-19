from regist import register_user
from sing_in import sing_in
from user_menu import  menu_user


print("Вітаємо на наші платформі !")
while True:
    menu=input("""     
     Оберіть дії:
     
     1. Реєстрація нового користовича
     2. Аутентифікація
     3. Вихід з платформи
Введіть варіант: """)

    if menu=="1":
        print("Процес реєстрації нового користувача: ")
        print()
        register_user()
        # print("Для продовження необхідна аутентифікація")
        # while True:
        #     email_user = input("Enter your email: ")
        #     password = input("Enter your password: ")
        #     res=sing_in(email_user,password)
        #     if res=="Вхід успішний":
        #         break
        #     else:
        #         print("Користувача не знайдено!")
        # menu_user(email_user)
    if menu =="2":
        while True:
            email_user = input("Введіть email: ")
            password = input("Введіть пароль: ")
            res=sing_in(email_user,password)
            if res=="Вхід успішний":
                break
            else:
                print("Користувача не знайдено!")
        menu_user(email_user)
    if menu=="3":
        print("До побачення!")
        break




