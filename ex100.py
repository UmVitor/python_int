#Faça um programa que tenha uma lista chamada numeros e duas funções 
#chamadas sorteia() e somaPar(). A primeira função vai sortear 5 numeros 
#e coloca-los dentro de uma lista e a segunda função vai mostrar a soma entre 
#todos os valores pares sorteados pela função anterior

from random import randint

lista = list()
soma = 0
def sorteia():
    print('Sorteando 5 valores ', end=' ')
    for c in range(0,5):
        lista.append(randint(0,10))
        print(lista[c] , end=' ')
    print()

def somaPar():
    soma = 0
    print(f'Somando os valores pares de {lista}, temos ', end=' ')
    for c in range(0,len(lista)):
        if((lista[c]%2) == 0):
            soma += lista[c]
    print(soma)

sorteia()
somaPar()
