#crie um programa que leia duas notas de um aluno e calcule sua média 
#mostrando uma mensagem no final, de acordo com a media atingida
#Media abaixo de 5 - Reprovado
#Media entre 5 e 6.9 - Recuperação 
#Media entre 7 ou superior - Aprovado

n1 = float(input('Primeira unidade: '))
n2 = float(input('Segunda unidade: '))
n3 = float(input('Terceira Uniade: '))

media = (n1 + n2 + n3)/3

if(media < 5):
    print('Reprovado')
elif(5<=media<=6.9):
    print('Recuperação')
else:
    print('Aprovado!!!')