#Faça um programa que jogue par ou impar com o computador. O jogo só será
#interrompido quando o jogador perder, mostrando o total de vitorias consecutivas 
#que ele conquistou no fianl do jogos
import random
print('-='*20)
print('Vamos jogar par ou impar'.upper())
cont = 0 
while True:
    val = int(input('Digite um valor: '))
    esc = str(input('Par ou impar? [P/I]: ')).upper()
    esc = esc.replace('P','PAR')    
    esc = esc.replace('I','IMPAR') 
    rand = random.randint(1,10)
    total = rand + val
    if (total%2 == 0):
        total_str = 'PAR'
    else:
        total_str = 'IMPAR'
    if ((esc == total_str) or (esc == total_str)):
        print(f'Você jogou {val} e o computador {rand}. total de {total} de {total_str}')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('-='*20)
        print(f'Você jogou {val} e o computador {rand}. total de {total} deu {total_str}')
        print('Você Perdeu!')
        print(f'Gamer Over!! Você venceu {cont} vezes.')
        break


