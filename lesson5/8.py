initial = int(input())
end = int(input())
sumi = 0
for i in range(initial, end + 1, 2):
    print(i)
    sumi = sumi + i
