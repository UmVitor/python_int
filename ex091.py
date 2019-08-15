#Crie um programa onde 6 jogadores joguem um dado e tenham resultados aleatorios
#Guarde esses resultados em um dicionario. Guarde esses resultados num dicionario
#No final, coloque esse dicionario em ordem. Sabendo que o vencedor tirou o maior
#numero no dado.

from time import sleep
import random
jogadores = dict()
grupo = list()
aux = dict()
for c in range(0,6):
    jogadores['Nome'] = "Jogador{}".format(c+1)
    jogadores['result'] = random.randint(1,6)    
    grupo.append(jogadores.copy())

print('Valores Sorteados: ')
for c in range(0,6):
    print(" "*3,f"O {grupo[c]['Nome']}  tirou {grupo[c]['result']}")
    sleep(1)

for c in range(0,6):
    for k in range (c,6):
        if (grupo[c]['result'] < grupo[k]['result']):
            aux = grupo[c].copy()
            grupo[c] = grupo[k].copy()
            grupo[k] = aux.copy()
           
print('Ranking com os jogadores:')
for c in range(0,6):
    print(' '*3,f"{c+1}° lugar {grupo[c]['Nome']} com {grupo[c]['result']}")
    sleep(1)

