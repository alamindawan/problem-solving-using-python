

num = int(input())
num += 1
for x in range(1,num):
    if x % 2 == 0:
        n = x * x
        print(str(x)+'^2 = '+str(n))


