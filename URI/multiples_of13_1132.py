
x = int(input())
y = int(input()) + 1

total = 0
for a in range(x,y):
    if a % 13 == 0:
        a = 0
    total += a
print(total)
