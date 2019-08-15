#Faça um programa que leia o ano qualquer e mostre se ele é bisexto 

from datetime import date
n1 = int(input('Digite um ano: '))
if (n1 == 0):
    n1 = date.today().year # Pega o ano atual
if( (n1%4 == 0)  and (not(n1%100 == 0  and n1%400 != 0))):
    print('Esse ano é bisexto!!!')
else:
    print('Esse ano não é bisexto!!')
