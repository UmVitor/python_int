#Faça um programa que tenha uma função chamada contador(), que receba tres
#parametros: inicio, fim e passo e realize contagem.
#seu programa tem que realizar três contagens atraves da função criada
#a) de 1 ate 10, de 1 em 1 
#B) de 10 até 0 de 2 em 2 
#c) um contagem personalisada

from time import sleep

def contador(inicio, fim,passo):
    print('-='*30)
    if (passo == 0):
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if (fim>inicio):
        for c in range(inicio, fim+passo, passo):
            if(c > fim):
                continue
            else:
                print(f'{c}',end=' ')
            sleep(1)
        print()
    elif(fim<inicio):
        passo = -passo
        for c in range(inicio, fim+passo, passo):
            if(c < fim):
                continue
            else:
                print(f'{c}',end=' ')
            sleep(1)
        print()
    print('-='*30)
    



contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = abs(int(input('Passo: '))) 
contador(i,f,p)


