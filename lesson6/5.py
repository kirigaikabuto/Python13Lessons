arr = [123, 24, 45, 232]
print(arr)
for i, v in enumerate(arr):
    if v % 2 == 0:
        arr[i] = 0
print(arr)
