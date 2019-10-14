
n = 1
while n != 0:
    num = int(input())
    if num > 0:
        for x in range(1,num+1):
            if num == x:
                tt = ''
            else:
                tt = ' '
            print(x,end=tt)
        print()
    else:
        n = num
