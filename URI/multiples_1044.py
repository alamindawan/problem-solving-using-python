
A,B = input().split()
n1 = int(A)
n2 = int(B)
if n2 % n1 == 0:
    print('Sao Multiplos')
elif n1 % n2 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')



