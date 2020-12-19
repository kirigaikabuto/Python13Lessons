numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = ""
for i in numbers:
    s = s + str(i) + " "
file = open("numbers.txt", "w")
file.write(s)
file.close()
