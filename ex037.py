#Escreva um programa que leia um número inteiro qualquer e peça para o
#usuario escolher qual será a base de conversão
#1 para binario 
#2 para octal
#3 para hexadecimal

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite\n 1 para binario\n 2 para octal\n 3 para hexadecimal: '))

if (n2 == 1):
    print(bin(n1))
elif(n2 == 2):
    print(oct(n2))
elif (n2 == 3):
    print(hex(n2))
else:
    print('Opção inválida')