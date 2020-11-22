a = input()
# первая проверка
if a != "":
    if a.isnumeric():
        a = int(a)
    else:
        print("Please write only numbers")
        exit()
else:
    print("Please write something")
    exit()

print(a + 1)
