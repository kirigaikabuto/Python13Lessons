from functools import reduce


def GetSum(a, b):
    return a + b


def getMax(a, b):
    if a > b:
        return a
    else:
        return b


arr = [1, 2, 3, 4]
sumi = reduce(GetSum, arr)
maxi = reduce(getMax, arr)
print(maxi)
# getMax
# a=1,b=2 -> 1>2 -> 2
# a=2,b=3 -> 2>3 -> 3
# a=3,b=4 -> 3>4 -> 4
# a, b -> 1, 2 -> return 1 + 2 ->3
#
# 3, 3 -> return 3 + 3 -> 6
# 6, 4 -> return 6 + 4
