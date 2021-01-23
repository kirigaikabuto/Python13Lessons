def checkEven(a):
    if a % 2 == 0:
        return True
    else:
        return False


def check2(a):
    if a > 2:
        return True
    else:
        return False


arr = [1, 2, 3, 4, 2, 4, 5, 6, 7, 7, ]
newArr = list(filter(checkEven, arr))
print(newArr)
newArr = list(filter(check2, arr))
print(newArr)
