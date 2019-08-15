#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
#Depois disso, mostre a listagem de numeros gerados e tambem indique o menor 
#e o maior valor em questão da tupla

import random
n = ( random.randint(0,10) , 
      random.randint(0,10) , 
      random.randint(0,10) ,
      random.randint(0,10) , 
      random.randint(0,10))
k = sorted(n)
print(f'Os valores sorteados foram {n}')
print(f'O menor valor sorteado foi {k[0]}')
print(f'O maior valor sorteado foi {k[4]}')

#De outra forma
print(f'Os valores sorteados foram {n}')
print(f'O menor valor sorteado foi {min(n)}')
print(f'O maior valor sorteado foi {max(n)}')