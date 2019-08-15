#faça um programa que leia 5 valores numericos e guarde-os em uma lista
#No final, mostre qual foi o maior e o menor valor digitado e as
#suas respectivas posições na lista

valores = list()
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: '))) 

print('=-'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end=' ')
a = valores.index(max(valores))
print(valores.index(max(valores)), end=' ')
for c in range (0 ,5):
    if (a != valores.index(max(valores),c)):
        print(valores.index(max(valores),c), end=' ')
        a = valores.index(max(valores),c)
print('\n')

print(f'O menor valor digitado foi {min(valores)} nas posições ', end=' ')
b = valores.index(min(valores))
k = min(valores)
for d in range (0, 5):
    if (valores[d] == k):
        print(d, end=' ')
        
