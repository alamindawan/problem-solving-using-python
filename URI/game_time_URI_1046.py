
duration = 24

x,y = input().split()

x = int(x)
y = int(y)

h = 0
if x < y:
    h = y - x
elif x > y:
    h = (24 - x) + y
else:
    h = 24
print('O JOGO DUROU '+str(h)+' HORA(S)')

