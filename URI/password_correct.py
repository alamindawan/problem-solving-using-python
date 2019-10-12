correct = 2002
n = 0
while n != correct:
    num = int(input())

    if num == correct:
        print('Acesso Permitido')
        n = num
    else:
        print('Senha Invalida')
