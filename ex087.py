#Aprimore o desafio anterior, mostrando no final
#A) A soma de todos os valores pares digitados
#B) A soma dos valores da terceira coluna 
#C) O maior valor da segunda linha

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0 
soma3 = 0 
maior = 0
for c in range(0,3):
    for k in range(0,3):
        matriz[c][k] = int(input(f'Digite um valor para [{c}, {k}]: '))
        if (matriz[c][k]%2 == 0):
            soma += matriz[c][k]
        if (k == 2):
            soma3 += matriz[c][k]
        if(c == 1):
            if(matriz[c][k] > maior):
                maior = matriz[c][k]
print('-='*20)
for c in range(0,3):
    for k in range(0,3):
        print(f'[ {matriz[c][k]:^5} ]', end='')
    print()
print('-='*20)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluno é {soma3}.')
print(f'O maior valor da segunda linha é {maior}.')