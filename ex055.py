#Faça um programa que leia o peso de cinco pessoas. NO final, mostre qual foi
#o maior e o menor peso lidos

for c in range (0,5):
    peso = float(input('Digite seu peso: '))
    if(c == 0):
        maior = peso
        menor = peso
    if (peso > maior):
        maior = peso
    elif (peso < menor ):
        menor = peso

print('O maior peso lido foi de {}'.format(maior))
print('O menor peso lido foi de {}'.format(menor))