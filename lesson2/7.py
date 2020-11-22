name = input("введите свое имя:")
if name != "":
    if not name.isalpha():
        print("Please write only alphabets characters")
        exit()
else:
    print("Please write something")
    exit()
year = input("введите год рождения:")
if year != "":
    if year.isnumeric():
        year = int(year)
    else:
        print("Please write only numbers")
        exit()
else:
    print("Please write something")
    exit()
age = 2020 - year
output = f"Вас зовут {name} и вам сейчас {age}"
print(output)
# name.isalpha()->для букв
# name.isnumeric()->для цифр
# введите свое имя:Ерасыл
# введите год рождения:1998
#
# Вас зовут Ерасыл и вам сейчас 22
