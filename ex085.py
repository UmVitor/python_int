#Crie um programa onde o usuario possa digitar sete valores numéricos e 
#cadastre-os em uma lista única que mantenha separados os valores pares e 
#impares. No final, mostree os valores pares e impares em ordem crescente

grupo = [[], []]
for c in range (0,7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if (n%2 == 0):
        grupo[0].append(n)
    else:
        grupo[1].append(n)

grupo[0].sort()
grupo[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {grupo[0]}')
print(f'Os valores impares digitados foram: {grupo[1]}')

