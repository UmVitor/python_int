#Crie um programa que simule o funcionamento de um caiza eletronico. No inicio
#inicio, pergunte ao usuario qual será o valor a ser sacado(numero inteiro)
#e o programa vai informar quantas cédulas de cada valor serão integres
#Obs: considere que o caiza possui cédulas de R$50, R$20 , R$10 e R$1.

print('='*30)
print('{:^30','BANCO CEV',''*10)
print('='*30)
c_1 = c_10 = c_20 = c_50 = 0
n1 = int(input('Que valor você quer sacar? R$ '))
c_50 = n1//50
n1 = n1%50
c_20 = n1//20
n1 = n1%20
c_10 = n1//10
n1 = n1%10
c_1 = n1//1
if (c_50 != 0):
    print(f'Total de {c_50} cédulas de R$50')
if (c_20 != 0):
    print(f'Total de {c_20} cédulas de R$20')
if (c_10 != 0):
    print(f'Total de {c_10} cédulas de R$10')
if(c_1 != 0):
    print(f'Total de {c_1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')