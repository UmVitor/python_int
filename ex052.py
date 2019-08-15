#Faca um programa que leia um numeor inteiro e diga se ele é ou não primo
n1 = int(input('Insira um numero: '))
aux = 0
for c in range(n1 , 1 , -1):
    if (n1%c == 0 and n1 != c):
        aux = 1
if(aux == 0):
    print('{} é primo'.format(n1))
else:
    print('{} não é primo'.format(n1)) 