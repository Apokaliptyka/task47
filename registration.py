import json
import string
from test import name


def register_user():
    with (open("data.json", "r",encoding='utf-8') as file_data):
        sumbols = "abcdefghijklmnopqrstuvwxyz0123456789@."

        data_users = json.load(file_data)
        print(data_users)
        user_data = {}

        id_user = 1
        if len(data_users) > 0:
            id_user = data_users[-1]["id"] + 1

        while True:
            user_name = input("Введіть своє ім'я та прізвище : ")
            print()
            full_name = string.capwords(user_name)
            audit_name = ""
            for item in full_name:
                if item not in (string.digits or string.punctuation):
                    audit_name += item
            if audit_name == full_name:
                break
            print("Помилка формату імені! Повторіть спробу")
            print()

        while True:
            unique_email = ""
            audit_email = ""
            email_user = input("Введіть свій email: ")
            print()
            for item in email_user:
                if item in sumbols:
                    audit_email += item
            if len(data_users)>0:
                for user in data_users:
                    if user["email"]==email_user:
                        unique_email = email_user
            if audit_email == email_user and email_user.count("@") == 1 and len(unique_email) == 0:
                break
            else:
                print("Неправильний формат email або такий email уже існує! \nПеревірте та спробуйте ввести його знову!")
                print()
        while True:
            audit_password = ""
            password_user = input("""
(пароль повинен починатися з великої літери та містити від 8 до 16 символів!)
Введіть пароль: """)
            password_user2 = input("""
Повторно введіть пароль: """)
            if password_user != password_user2:
                print()
                print("Паролі не співпадають!")
            else:

                for item in password_user:
                    if item in string.printable:
                        audit_password += item
                len_pass = len(password_user)

                if password_user[0] in string.ascii_uppercase and (
                        8 <= len_pass <= 16) and audit_password == password_user:
                    break
                else:
                    print()
                    print("Неправильний формат паролю!")


        user_data['id'] = id_user
        user_data['full name'] = full_name
        user_data['email'] = email_user
        user_data['password'] = password_user
        data_users.append(user_data)

    with open("data.json", "w") as file_data:
        json.dump(data_users, file_data, indent=4)
        print()
        print("""
      Вітаємо !
Авторизація успішна !    """)


# register_user()
