#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados
#de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final mostre:
#A) Quantas pessoas foram cadastradas 
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres 
#D) Uma lista com todas as pessoas com idade acima da media

pessoas = dict()
grupo = list()
mulheres = list()
sair = 's'
soma = 0
media = 0
while True:
    pessoas['nome'] = str(input('nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] '))
    pessoas['idade'] = int(input('Idade: '))
    sair = str(input('Quer continuar? [S/N] '))
    grupo.append(pessoas.copy())
    if (pessoas['sexo'] in 'Ff'):
        mulheres.append(pessoas['nome'])
    
    soma += pessoas['idade']
    
    if (sair in 'Nn'):        
        break

media = soma/len(grupo)
print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A media de idade é de {media:.2f} anos')
print('- As mulheres cadastradas foram:', end=' ')
for c in range(0 ,len(mulheres)):
    print(mulheres[c],end=' ')
print()
print('- lista das pessoas que estão acima da média: ')
for c in range (0, len(grupo)):
    if (grupo[c]['idade'] > media):
        print(f'nome = {grupo[c]["nome"]}; sexo = {grupo[c]["sexo"]}; idade = {grupo[c]["idade"]}')
        print()