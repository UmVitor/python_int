#Crie um programa que tenha uma tupla totalmente preenchida com uma
#contagem por extenso, de zero ate vinte.
#Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostrálo
#por extenso
extenso = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n1 = int(input('Digite um número entre 0 e 20: '))
while(n1 > 20 or n1 < 0):
    n1 = int(input('Tente novamente!!\nDigite um numero entre 0 e 20: '))
print(f'você digitou o número {extenso[n1]}!!')
