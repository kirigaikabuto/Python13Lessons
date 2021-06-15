arr = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 1]
]
result = []
for element_arr in arr:
    sumi = 0
    for value in element_arr:
        sumi += value
    result.append(sumi)
print(result)
