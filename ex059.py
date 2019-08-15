#Crie um programa que leia dois valores e mostre um menu na tela
#[1] somar
#[2] multiplicar 
#[3] maior
#[4] novos numeros
#[5] sair do programa

sair = 0
while(sair == 0):
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa\n')
    op = int(input('Digite uma opção: '))
    if (op == 1):
        tot = n1 + n2
        print(tot)
    elif(op == 2):
        tot = n1 * n2
        print(tot)
    elif(op == 3):
        if(n1 > n2):
            print(n1)
        else:
            print(n2)
    elif(op == 4):
        continue
    else:
        print('Saindo do programa!!!!')
        sair = 1