#Crie um programa onde o usuario possa digitar varios valores numericos
#e cadrastre-os em uma lista. Caso o número já exista lá dentro, ele
#não será adicionado. No final, serão exibidos todos os valores 
#unicos digitados, em ordem crescente

sair = 's'
listas = []
while (sair != 'n'):
    n = int(input('Digite um valor: '))
    if (listas.count(n) == 0):
        listas.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não é possível adicionar...')
    sair = str(input('Quer continuar? [S/N] ')).lower()
listas.sort()
print('-='*20)
print(f'Você digitou os valores {listas}')