n = int(input())
c = False
sumi = 0
for i in range(0, n + 1):
    c = True if i % 2 == 0 else False
    if c:
        print(i)
        sumi = sumi + i
