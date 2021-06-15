numbers = [1, 2, 34, 5, ]
numbers2 = [1, 2, 34, 5, ]
print("numbers")
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1
    print(numbers[i])

print("numbers2")
for i in numbers2:
    i = i + 1
    print(i)

print("numbers", numbers)

print("numbers2", numbers2)