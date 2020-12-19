numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbersStrt = []
for i in numbers:
    numbersStrt.append(str(i))
s = "\n".join(numbersStrt)
file = open("numbers.txt", "w")
file.write(s)
file.close()
