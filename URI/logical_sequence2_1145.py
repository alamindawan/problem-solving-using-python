x,y = input().split()
num1 = int(x)
num2 = int(y) + 1
for a in range(1,num2):
    if a % num1 == 0:
        tt = ''
    else:
        tt = ' '
    print(a,end=tt)
    if a % num1 == 0:
        print()
