#Refaça o Desafio 51. Lendo o primeiro termo e a razãp de uma PA, mostrando
#os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
count = 0
while(count != 10 ):
    print(a1)
    a1 = a1 + r
    count += 1