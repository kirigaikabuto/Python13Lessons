s = "16"
print(s.isalpha())
print(s.isnumeric())
#
pred = "Я родился в городе А в 1967 году. В возрасте 5 лет я уехал в город B"
numbers = []  # [1967,5]
# разбить предложения по пробелам
# пройтись по каждом слову и проверить является ли оно числом
# и если это число то закинуть в массив numbers
