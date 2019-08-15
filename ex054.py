#Faca um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
#pessoas ainda não atigiram a maioridade(21 anos) e quantas já são maiores


from datetime import date
ano_atual = date.today().year 
n1 = 0
n2 = 0
for c in range (1,8):
    ano = int(input('Isira o seu ano de nascimento: '))
    if((ano_atual - ano) >= 21):
        n1 += 1
    else:
        n2 += 1
print ('O numero de pessoas acima da maioridade: {}'.format(n1))
print ('O numero de pessoas abaixo da maioridade: {}'.format(n2))