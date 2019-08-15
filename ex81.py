#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, mostre
#A)Quantos números foram digitados
#B)A lista de valores ordenada de forma decrescente.
#C)Se o valor 5 foi digitado e está ou não na lista.

sair = 's'
lista = []
while (sair != 'n'):
    lista.append(int(input('Digite um valor: ')))
    sair = str(input('Quer continuar? [S/N] '))
print('-='*20)
lista = sorted(lista,reverse=True)
print(f'Os valores em ordem crescente são {lista}')
if(lista.count(5) != 0):
    print('O valor 5 faz parte da lista!!')
else:
    print('O valor 5 não faz parte da lista!!')
