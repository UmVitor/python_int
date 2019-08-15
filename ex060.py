#Faça um programa que leia um numero qualquer e mostre o seu fatorial

n1 = int (input('Digite um numero: '))
aux = 1
while(n1 != 0 ):
    aux = aux * n1
    n1 = n1 - 1
print('O fatorial é {}'.format(aux))
    