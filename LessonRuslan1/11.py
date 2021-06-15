arr = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
arr2 = filter(lambda x: x % 2 == 0, arr)
print(list(arr2))
