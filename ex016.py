#Crie um programa que leia um numero real
#Qualquer pelo teclado e mostre na tela 
#a sua porção inteira
import math
num = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(num,math.floor(num)))
