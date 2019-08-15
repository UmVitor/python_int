#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os 
#valores lidos no teclado. No final, mostre a matriz na tela, com a 
#formatação correta

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(0,3):
    for k in range(0,3):
        #matriz[c][k] = 1
        matriz[c][k] = int(input(f'Digite um valor para [{c}, {k}]: '))

for c in range(0,3):
    for k in range(0,3):
        print(f'[ {matriz[c][k]:^5} ]', end='')
    print()
