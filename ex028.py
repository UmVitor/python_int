#escreva um programa que faça o computador 'pensar' em um numero inteiro
#entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido
#pelo computador.

import random
from time import sleep
n1 = int(input('Digite um numero: '))
n2 = random.randint(1,5)
print ('Pensando...')
sleep(2)
print('O numero escolhido foi {}'.format(n2))
if (n2 == n1):
    print('Você acertou')
else:
    print('Você errou')