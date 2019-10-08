m,n = input().split()
m = int(m)+1
n = int(n)

total = 0
my = ''
if n >= 1 and m >= 1:
    for x in range(n,m):
        total += x
        my += str(x)+' '
    print(my+'Sum='+str(total))



