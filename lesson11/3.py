# username
# password
# #1) авторизация или регистрация
# [1]авторизация
# [2]регистрация
# #2) если бы выбрана авторизация то мы должны проверить существует ли данный пользователь в нашей системе
# если пользователь есть -> добро пожаловать {username}
# если пользователя нету -> у нас нет такого пользователя
import json

user1 = {
    "username": "user1",
    "password": "user1"
}
user2 = {
    "username": "user2",
    "password": "user2"
}
user3 = {
    "username": "user3",
    "password": "user3"
}
users = [user1, user2, user3]
fileName = "users.json"
usersJson = json.dumps(users, indent=4)
file = open(fileName, "w")
file.write(usersJson)
file.close()
