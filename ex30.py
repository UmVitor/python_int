#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou imapar

n1 = int(input('Digite um numero: '))
res = n1%2
if (res == 0):
    print('Esse numero é par!!')
else: 
    print('Esse numero é impar!!')