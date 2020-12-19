file = open("numbers.txt", "r")
data = file.read()
file.close()
numbersStr = data.split(" ")
numbersStr.remove("")
numbers = []
for i in numbersStr:
    numbers.append(int(i))
print(numbers)
