a = b = c = t = outPut = sub = ''
a,b,c = input().split();
t = int(a) + int(b) + int(c)
if t % 2 == 0:
    outPut = int(t / 2)
else:
    sub = t - 1
    outPut = int(sub / 2)
print(outPut)



