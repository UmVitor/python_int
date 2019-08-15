#Crie um programa que leia varios numeros inteiros pelo teclado. No final da 
#execução, mostre a média entre todos os valores e qual foram o maior e o menor 
#valores lidos. O programa deve perguntar ao usuario se ele quer ou não
#continuar a digitar valores.

cont = 0
sair = 0
media = 0
n1 = int(input('Digite um numero: '))
maior = n1
menor = n1
while(sair != 999):
    cont += 1
    media +=  n1
    if (maior < n1 ):
        maior = n1
    elif (menor > n1):
        menor = n1
    n1 = int(input('Digite um numero: '))
    sair = n1
media = media/cont
print('Média: {}\nMaior: {}\nMenor: {}'.format(media,maior,menor))
