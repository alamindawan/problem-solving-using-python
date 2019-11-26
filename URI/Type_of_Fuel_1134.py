num1 = 0
al = gas = dis = 0
while num1 != 4:
    num = int(input());
    if num == 1:
        al = al + 1
    elif num == 2:
        gas = gas + 1
    elif num == 3:
        dis = dis + 1
    num1 = num
print('MUITO OBRIGADO')
print('Alcool: ' + str(al))
print('Gasolina: ' + str(gas))
print('Diesel: ' + str(dis))

