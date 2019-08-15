#Melhore o jogo do desafio 028 onde o computador vai pensar em um
#numero entre 0 e 10. Só que agora o jagador vai tentar advinhar ate acertar
#Mostrando no final quantos palpites foram necessarios para vencer

import random
num = random.randint(0,10)
cont = 1
n1 = int(input('Digite um numero: '))
while(n1 != num):
    n1 = int(input('Digite um numero: '))
    cont += 1
print('Parabéns voce acertou com {} tentativas'.format(cont))