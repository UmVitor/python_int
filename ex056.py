#Desenvolva um programa que leia o nome, idade e sexo  de 4 pessoase no final 
#moste: A media de idade do grupo, Qual o nome do homem mais velho,  Quantas mulheres tem menos de 25anos
somaidade = 0 
media = 0 
maioridadehomem = 0 
nomevelho = ''
totmulher20 = 0
for p in range(1 , 5):
    nome = str(input("Nome: ")).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M /F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
media = somaidade/4
print('A media de idade do grupo é: {}'.format(media))
print('O homem mais velho é {} e tem {} anos'.format(nomevelho,maioridadehomem))
print('Existem {} Mulheres com menos de 20 anos'.format(totmulher20))