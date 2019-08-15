#Faça um programa que leia o nome completo de uma pessoa, mostrando em 
#seguida o primeiro e o último nome separadamente

nome = str(input('Digite seu nome: ')).strip().split()
print('Primeiro: {}'.format(nome[0]))
print('Ultimo: {}'.format(nome[len(nome)-1]))
