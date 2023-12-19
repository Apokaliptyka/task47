import json

def deleted_user_data(login):
    with open("data.json", "r") as file_users:
        data_users = json.load(file_users)
        user_index = 0
        for user in data_users:
            if user["email"] == login:
                user_index = data_users.index(user)
        data_users.pop(user_index)
        print("Обліковий запис видалено!")
    with open("data.json", "w") as file_data:
        json.dump(data_users, file_data, indent=4)

