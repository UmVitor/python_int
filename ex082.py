#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, crie duas listas extras que vão contar apenas com os
#valores pares e os valores impares digitados, respectivamente.
#Ao final mostre o conteudo das três listas geradas
sair = 's'
lista =  []
impar =  []
par = []
while (sair != 'n'):
    lista.append(int(input('Digite um numero: ')))
    sair = str(input('Quer continuar? [S/N] '))

for c in range (0, len(lista)):
    if (lista[c]%2 == 0):
        par.append(lista[c])
    else:
        impar.append(lista[c])
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')

