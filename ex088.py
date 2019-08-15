#Faça um programa que ajude um jogador da mega-sena a criar palpites
#O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
#composta

import random
from time import sleep
print('-'*50)
print(f'{"JOGA NA MEGA SENA" :^50}')
print('-'*50)
jogos = int(input('Quantos jogos você deseja sortear? '))
n = 0 
numeros = []
mega = []
for k in range(0,jogos):
    for c in range(0,6):
        n = random.randint(0,60)
        while(numeros.count(n) != 0):
            n = random.randint(0,60)
        else:
            numeros.append(n)
    numeros.sort()
    mega.append(numeros[:])
    numeros.clear()
print('-='*8,f'Sorteando {jogos} jogos','-='*8)
for c in range(0,jogos):
    sleep(1)
    print(f'Jogo {c + 1}: {mega[c]}')
print('-='*10, 'BOA SORTE!' , '-='*10)

