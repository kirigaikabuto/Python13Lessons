
# Уравнения типа ax + b = 0 являются линейными уравнениями.
# Предложите пользователю ввести a и b (0> a> 10, 0> b> 10, например, a и b - однозначные положительные числа).
# Найдите решение уравнения и распечатайте его. (Не забудьте использовать блок try / except
# ax + b = 0
a = int(input("a="))
b = int(input("b="))
for x in range(-100, 0):
    c = a * x + b
    if c == 0:
        print(x)
