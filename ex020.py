#O mesmo professor do desafio anterior quer sortear a ordem de apresentação 
#dos trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada
import random

a1 = 'Alberto'
a2 = 'Creuza'
a3 = 'Joao'
a4 = 'Maria'
k = 4
print('{}'.format(random.sample([a1,a2,a3,a4],k)))
