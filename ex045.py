#Crie um programa capaz de jogar jokenpo
import random
n1 = random.choice(['Pedra','Papel','Tesoura'])
n2 = input('Escolha: ')

if (n1 == n2):
    print('Empate')
elif(n1 == 'Pedra' and n2 == 'Papel'):
    print('Você Perdeu!!!')
elif(n1 == 'Papel' and n2 == 'Pedra'):
    print('Você ganhou!!!')
elif(n1 == 'Pedra' and n2 == 'Tesoura'):
    print('Você Perdeu!!!')
elif(n1 == 'Papel' and n2 == 'Tesoura'):
    print('Você ganhou!!!')
elif(n1 == 'Tesoura' and n2 == 'Pedra'):
    print('Você ganhou!!!')
elif(n1 == 'Tesoura' and n2 == 'Papel'):
    print('Você Perdeu!!!')
else:
    print('Opção invalida!!!')