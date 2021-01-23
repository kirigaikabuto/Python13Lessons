def add1(n):
    return n + 1


arr = [1, 2, 3, 4]
newArr = map(add1, arr)
newArr = list(newArr)
print(newArr)
