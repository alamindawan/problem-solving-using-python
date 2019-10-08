
t = input()
ls = list(t)

n = 0
ab = sl = ''
for x in ls:
    #print(x.upper())
    if x.strip():
        if not ab:
            x = x.upper()
            ab = 1
        else:
            ab = ''

    sl += x
print(sl,'\n')
