nome = input('Digite o nome do aluno: ')
n1 = int(input('Digite a nota da primeira unidade: '))
n2 = int(input('Digite a nota da segunda unidade: '))
n3 = int(input('Digite a nota da terceira unidade: '))
s = (n1+n2+n3)/3
print('{} ficou com {:.2f} pontos na media.'.format(nome,s))