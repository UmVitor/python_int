#Faça um programa que leia o ano de nascimento de um jovem e informe, 
#de acordo com a sua idade.
#Se ele ainda vai se alistar ao serviço militar 
#Se é a hora de se alistar 
#Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo


n1 = int(input('Informe a sua idade: '))

if (n1 == 18):
    print('Está na hora de você se alistar!!!')
elif(n1 > 18):
    print('Você ultrapassou {} anos para se alistar!!'.format(n1 - 18))
else:
    print('Ainda não está na hora de se alistar, faltam {} anos!!'.format(18 - n1))
