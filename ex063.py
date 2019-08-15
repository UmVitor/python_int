#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela
#os n primeiros elementos de uma sequencia de fibonacci

n = int(input('Digite quantos elementos deseja mostrar: '))

count = 1
f1 = 0
f2 = 1
print('1', end=' ')
while(count != n):
    f = f1 + f2
    f1 = f2
    f2 = f
    print(', {}'.format(f),end=' ')
    count += 1