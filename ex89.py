#Crie um programa que leia nome e duas notas de vários alunos e guarde
#tudo em uma lista composta> no final mostre um boletim contendo a media de cada um
#e permita que o usuário possa mostrar as notas de cada aluno individualmente

alunos = list()
media = list()
notas = [[],[]]

grupo = list()
while True:
    nome = str(input("Nome do aluno: "))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    sair = str(input('Quer continuar? [S/N] ').lower())
    alunos.append(nome)
    notas[0].append(n1)
    notas[1].append(n2)
    media.append((n1+n2)/2)
    if (sair == 'n'):
        break

grupo.append(alunos[:])
grupo.append(notas[:])
grupo.append(media[:])
print('-='*20)
print('N° ', f'{"NOME" :<10}' , 'MÉDIA')
print('-'*20)
for c in range(0,len(alunos)):
    print(f'{(c + 1):<4}', end='')
    print(f'{grupo[0][c]:<10}', end=' ')
    print(f'{grupo[2][c]:.2f}', end=' ')
    print()

print('-'*40)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): ')) - 1
    if(n == 998):
        print('FINALIZANDO...')
        print('<<<< VOLTE SEMPRE >>>>>')
        break
    print(f'Notas de {grupo[0][n]} são {grupo[1][0][n], grupo[1][1][n]}')
    print('-'*20)