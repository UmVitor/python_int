#Faça um programa que leia o sexo de uma pessoa, mas so aceite 'M' ou 'F'
#Caso esteja errado, peça a digitação novamente.

sexo = str(input('Digite seu sexo:')).strip().lower()
while((sexo != 'm') and (sexo != 'f')):
    print('Opção inválida!!')
    sexo = str(input('Digite seu sexo:')).strip().lower()
    print(sexo)
print('Computado com sucesso!!')