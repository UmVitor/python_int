#refaça o desafio mostrando a tabuada de um numero que o usuario escolher 
n1 = int(input('Insira um numero: '))
for c in range (0,11):
    aux = c * n1
    print('{} * {} = {}'.format(n1,c,aux))