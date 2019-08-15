#Faça um programa que leia nome e peso de varias pessoas, guardando tudo 
#rm uma lista. No final , mostre.
#A) Quantas pessoas foram cadastradas
#B) Uma listagem com as pessoas mais pesadas
#C) Uma listagem com as pessoas mais leves

lista = list() # Lista temporária
grupo = list()
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    grupo.append(lista[:])
    lista.clear()
    sair = str(input('Quer continuar? [S/N]')) 
    if sair in 'Nn':
        break 

menor = int(grupo[0][1])
maior = int(grupo[0][1])
for c in range(0, len(grupo)): 
    if (grupo[c][1] < menor ):
        menor = grupo[c][1]
    elif(grupo[c][1] > maior ):
        maior = grupo[c][1]
    
print(f'Ao todo você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi {maior:.2f} Peso de ', end=' ')
for c in range (0 , len(grupo)):
    if(grupo[c][1] == maior):
        print(f'[{grupo[c][0]}]', end=' ')
print('\n')
print(f'O menor peso foi {menor:.2f} Peso de ',end=' ')
for c in range (0, len(grupo)):
    if(grupo[c][1] == menor):
        print(f'[{grupo[c][0]}]', end=' ')
