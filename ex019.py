#Um professor quer sortear um dos seus quatro alunos para apagar o quadro 
#Faça um programa que ajude ele, lendo os nomes deles e escrevendo o nome do escolhido

import random 
import math

a1 = 'Alberto'
a2 = 'Creuza'
a3 = 'Joao'
a4 = 'Maria'

print('{}'.format(random.choice([a1,a2,a3,a4])))
