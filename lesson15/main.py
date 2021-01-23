def getEvenNumbers(a):
    numbers = []
    for i in a:
        if i % 2 == 0:
            numbers.append(i)
    return numbers


def getSum(a):
    sumi = 0
    for i in a:
        sumi += i
    return sumi


arr = [1, 2, 3, 4]
evenNumbers = getEvenNumbers(arr)  # [2,4]
print(evenNumbers)
sumi = getSum(evenNumbers)
print(sumi)
