initial = int(input())
end = int(input())
sumi1 = 0
sumi2 = 0
for i in range(initial, end + 1):
    if i % 2 == 0:
        sumi1 += i
    else:
        sumi2 += i
print(sumi1)
print(sumi2)
