number1 = int(input("введите первое число:"))
number2 = int(input("введите второе число:"))
number3 = int(input("введите третье число:"))
maxi = 0
mini = 0
if number1 > number2 and number1 > number3:
    maxi = number1
elif number2 > number1 and number2 > number3:
    maxi = number2
else:
    maxi = number3

if number1 < number2 and number1 < number3:
    mini = number1
elif number2 < number1 and number2 < number3:
    mini = number2
else:
    mini = number3
print(f"максимальное число это {maxi}")
print(f"минимальное число это {mini}")
