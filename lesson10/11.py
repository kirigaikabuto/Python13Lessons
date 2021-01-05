# необхождимо создать приложение телефонной книжки
# где человек может искать как и по телефону так и по имени
#
# 1) по телефону
# 2) по имени
# 1
# введите номер: 8708234344
# номер 8708234344 принадлежит ____
#
#
# 1) по телефону
# 2) по имени
# 2
# введите имя: Yerassyl
# номер телефона у Yerassyl это _____

people1 = {
    "name": "kir",
    "age": 14
}
people2 = {
    "name": "kiri",
    "age": 12
}
people3 = {
    "name": "kiro",
    "age": 10
}
peoples = [people1, people2, people3]
print("[1]поиск по имени")
print("[2]поиск по возрасту")
number = input("выбор:")
if number == "1":
    name = input("введите имя:")
    for i in peoples:
        if i["name"] == name:
            print(i)
elif number == "2":
    age = int(input("введите возраст:"))
    for i in peoples:
        if i["age"] == age:
            print(i)
else:
    print("no variants")
