# авторизация
# 1) считать все данные из файла
# 2) преобразовать данные в массив
# 3) создать меню
# 4) условие на выбор авторизаци
# 5) запросы на вводе username и password
# 6) пройтись циклом по всем данным и если был найден пользователь вывести соотвествующее сообщение
# 7) сделать проверку по username и если такого человека нету то написать соотствующеее
# 1
import json

file = open("users.json", "r")
usersJson = file.read()
file.close()
# 2
users = json.loads(usersJson)
# 3
print("[1]Авторизация")
# 4
number = input("выбор:")
if number == "1":
    isUsername = False
    isPassword = False
    print("---АВТОРИЗАЦИЯ---")
    # 5
    username = input("username:")
    password = input("password:")
    # 6
    for i in users:
        if i["username"] == username:
            isUsername = True
            if i["password"] == password:
                isPassword = True
            break

    if isUsername:
        if isPassword:
            print(f"Добро пожаловать {username}")
        else:
            print("Неправильный пароль")
    else:
        print("У нас нет такого пользователя")
