#Crie um programa que leia a idade e o sexo de várias pessoas. A cada
#pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não 
#continuar. No final mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados
#C) Quantas mulheres tem menos de 20 anos

cont = cont_H = cont_M = 0
while True:
    print('-'*22)
    print('CADRASTRE UMA PESSOA')
    print('-'*22)   
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    while (sexo != 'M' and sexo != 'F'):
        sexo = str(input('Sexo: [M/F] ')).upper()
    if (idade > 18):
        cont += 1
    elif (sexo == 'M'):
        cont_H += 1
    elif(idade < 20 and sexo == 'F'):
        cont_M += 1
    sair = str(input('Quer continuar? [S/N] ')).upper()
    while (sair != 'S' and sair != 'N'):
        sair = str(input('Quer continuar? [S/N] ')).upper()
    if(sair == 'N'):
        break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {cont_H} homens cadastrados.')
print(f'E temos {cont_M} mulheres com menos de 20 anos.')