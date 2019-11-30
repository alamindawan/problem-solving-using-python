x = 0
y = 1
while x <= 2:
    j1 = round(x, 1) + y

    print('I='+str(round(x, 1))+' '+'J='+str(j1))
    if y == 3:
        y = 1
        x = x + 0.2
    else:
        y = y + 1


