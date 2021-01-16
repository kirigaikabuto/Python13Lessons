arr1 = [1, 2, 3, ]
arr2 = [1, 30, 20, ]


def getMax(arr):
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    print(maxi)


getMax(arr1)
getMax(arr2)
