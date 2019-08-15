#Crie um programa que leia o nome completo de uma pessoa e mostre
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas 
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input('Digite o seu nome: ')
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
nome = nome.split()
print(nome[1])
