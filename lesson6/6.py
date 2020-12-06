arr = [123, 24, 45, 232]
maxi = arr[0]
for i, v in enumerate(arr):
    if v > maxi:
        maxi = v
print(maxi)
