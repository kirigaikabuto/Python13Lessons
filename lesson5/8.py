initial = int(input())
end = int(input())
sumi = 0
if initial % 2 != 0:
    initial += 1
if end % 2 != 0:
    end -= 1
for i in range(initial, end + 1, 2):
    print(i)
    sumi = sumi + i

# 3 10
# 4  6 8 10
# #5 20
# 6 8 10 12 14
