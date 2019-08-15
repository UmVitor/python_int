#Desenvolva um programa  que leia quatro valores pelo teclado e guarde-os em uma tupla> no final mostre
#A) Qunatas vezes apareceu o valor 9
#B) Em que posição foi digitado o primeiro valor
#C)Quais foram os numeros pares

n = (int(input('insira um numero: ')) ,
     int(input('insira um numero: ')) ,
     int(input('insira um numero: ')) ,
     int(input('insira um numero: ')))
print('O valor 9 apareceu {} vezes'.format(n.count(9)))
print('O valor 3 apareceu  na {}° posição'.format(n.index(9)))
print(f'os valores pares digitados foram:',end=' ')
for c in n:
    if c%2 == 0:
        print(c,end=' ')