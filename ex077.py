#Crie um programa que tenha uma tupla com vários palavras(não usar acentos)
#Depois disso, você deve mostrar, para cada palavra quais são as suas vogais
n = ('macarrao', 'azul', 'verde')
for c in n:
    print('Na palavra {} temos:'.format(c.upper()), end=' ')
    if c.count('a') > 0:
        print('a', end=' ')
    if c.count('e') > 0:
        print('e', end=' ')
    if c.count('i') > 0:
        print('i', end=' ')
    if c.count('o') > 0:
        print('o', end=' ')
    if c.count('u') > 0:
        print('u', end=' ')
    print(' ')

#de outra forma 
for p in n:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (letra ,end=' ')