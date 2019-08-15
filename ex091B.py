#Crie um programa onde 6 jogadores joguem um dado e tenham resultados aleatorios
#Guarde esses resultados em um dicionario. Guarde esses resultados num dicionario
#No final, coloque esse dicionario em ordem. Sabendo que o vencedor tirou o maior
#numero no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6),   
        'jogador2': randint(1,6),   
        'jogador3': randint(1,6),   
        'jogador4': randint(1,6),   
        'jogador5': randint(1,6),   
        'jogador6': randint(1,6),}
ranking = list()
print('valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)  #intemgetter significa a posição do dicionario que irá ordenar
print('-='*10)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)