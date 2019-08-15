#Crie um programa que leia o nome de uma cidade e diga se ela começa ou
#não com o nome "santo"

nome = input('Digite seu nome: ')
nome = nome.split()
print('Seu nome começa com Silva? {}!'.format(nome[0] == 'Silva'))
