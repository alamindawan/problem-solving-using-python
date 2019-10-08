for x in range(1,101):
    c = 0
    for y in range(2, (x // 2)):
        if x % y == 0:
            c = c + 1
            break
    if c == 0 and x != 1:
        print(x)



