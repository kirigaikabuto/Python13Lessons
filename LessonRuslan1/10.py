# def getSum(a):
#     sumi = 0
#     for i in a:
#         sumi += i
#     return sumi


arr = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 1]
]

results = map(lambda x: sum(x), arr)
print(list(results))
