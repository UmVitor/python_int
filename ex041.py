#A confederação nacional de natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria , de acordo com a idade
#Ate 9 anos - Mirim
#Ate 14 anos - infantil 
#Ate 19 anos - Junior 
#Ate 20 anos - Senior
#acima - Master

idade = int(input('Digite a idade: '))
if(idade <=9 ):
    print('Mirim')
elif(9<idade<14):
    print('Infantil')
elif(14<=idade<19):
    print("Junior")
elif(19<=idade<=20):
    print('Sênior')
else:
    print('Master')