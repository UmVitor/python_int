#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. NO
#final mostre os 10 primeiros termos dessa progressão

a1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
an = a1 + 9*r
for c in range (a1,an+1,r):
    print('{}'.format(c))