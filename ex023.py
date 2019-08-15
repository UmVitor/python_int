#Faça um programa que leia um numero de 0 9999 e mostre na tela cada um
#dos digitos separados.
import math
num = int(input('Digite um numero: '))

milhar = (num%10000)//1000
centena = (num%1000)//100
dezena = (num%100)//10
unidade = num%10
print('Analisando o numero {}'.format(num))
print('Unidade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}'.format(milhar))