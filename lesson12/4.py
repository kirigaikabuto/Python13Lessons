# авторизация
# 1) считать все данные из файла
# 2) преобразовать данные в массив
# 3) создать меню
# 4) условие на выбор авторизаци
# 5) запросы на вводе username и password
# 6) пройтись циклом по всем данным и если был найден пользователь вывести соотвествующее сообщение
# 7) сделать проверку по username и если такого человека нету то написать соотствующеее
# регистрации
# 1) создать меню
# 2) написать в условие на регистрации считывание данных о пользователе username,password
# 3) необходимо проверить не занято ли уже такой username
# 4) если все проверки были сделаны нормально в массив добавить новый элемент и сохранить в файл
import json

file = open("users.json", "r")
usersJson = file.read()
file.close()
# 2
users = json.loads(usersJson)
# 3
print("[1]Авторизация")
print("[2]Регистрация")
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
        # 7
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
elif number == "2":
    print("---РЕГИСТРАЦИЯ---")
    # 5
    username = input("username:")
    password = input("password:")
    isUsernameExist = False
    for i in users:
        if i["username"] == username:
            isUsernameExist = True
            break

    if isUsernameExist:
        print("у нас уже есть пользователь с таким username")
    user = {
        "username": username,
        "password": password,
    }
    users.append(user)
    file = open("users.json", "w")
    jsonUsers = json.dumps(users)
    file.write(jsonUsers)
    file.close()
    print("Регистрация прошла успешно")
else:
    print("нет такой команды")
