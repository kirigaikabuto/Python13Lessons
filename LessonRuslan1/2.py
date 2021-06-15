import math


def printHello():
    print("sdsds")


def getSum(a, b):
    return a + b


def getMultiple(a, b):
    return a * b


def getDifference(a, b):
    return math.fabs(a - b)


# a - integer
# b - integer
# operation -> def
def makeOperation(a: int, b: int, operation):
    return operation(a, b)


result = makeOperation(3, 4, getMultiple)
print(result)
