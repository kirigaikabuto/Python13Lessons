start = int(input())
end = int(input())
counterChet = 0
counterNeChet = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        counterChet += 1
    if i % 2 != 0:
        counterNeChet += 1
print(f"количество четных {counterChet}")
print(f"количество нечетных {counterNeChet}")
# 3
# 10
#
# 3 4 5 6 7 8 9 10
#
# четные:4
# нечетные:4
#
# 10
# 40
