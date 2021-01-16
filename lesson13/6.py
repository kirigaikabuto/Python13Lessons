arr1 = [1, 2, 3, ]
arr2 = [1, 30, 20, ]


def getMax(arr):
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    return maxi


def getAverage(arr):


maxi1 = getMax(arr1)
maxi2 = getMax(arr2)
print(maxi1, maxi2)
