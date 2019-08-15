#Faça um programa que leia nome e média de um aluno, guardando também a
#situação em um dicionario. No final mostre o conteudo da estrutura na tela
situacao = dict()
situacao['nome'] = str(input('Nome: '))
situacao['media'] = float(input('Média de {}: '.format(situacao['nome'])))
print('Nome é igual a {}'.format(situacao['nome']))
if (situacao['media'] >= 7):
    situacao['sit'] = 'Aprovado'
else:   
    situacao['sit'] = 'Reprovado'
print('Situação é igual a {}'.format(situacao['sit']))