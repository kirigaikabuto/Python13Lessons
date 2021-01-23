def chechEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


def divide2(number):
    return number // 2


arr = [2, 4, 6, 8]
# 1,2,3,4
# map(функция которая будет влиять на каждый элемент массива, массив)
newArr = map(divide2, arr)
newArr = list(newArr)
print(newArr)
