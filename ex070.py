#Crie um programa que leia o nome e o proço de varios produtos. O programa
#deverá perguntar se o usuário vai continuar. No final mostre:
#A) Qual é o total gasto na compra 
#B) Quantos produtos custam mais de R$1000
#C) Qual é o nome do produto mais barato
print('-'*20)
print(''*3,'LOJA SUPER BARATÃO',''*3)
print('-'*20)
cont= cont_mil = 0

produto = str(input('Nome do produto: '))
preco = int(input('Preço: R$ '))
menor = preco
menor_nome = produto
while True:
    sair = str(input('Quer continuar: [S/N] ')).upper()
    while ( sair != 'S' and sair != 'N'):
        sair = str(input('Quer continuar: [S/N] ')).upper()
    if (sair == 'N'):
        break
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    cont += preco
    if (preco > 1000):
        cont_mil += 1
    if (preco < menor):
        menor = preco
        menor_nome = produto
print(f'O total da compra foi de R$ {cont:.2f}')
print(f'Temos {cont_mil} prdutos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor_nome} que custa R${menor:.2f}')