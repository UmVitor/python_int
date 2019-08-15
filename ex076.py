#Crie um programa que tenha uma tupla única com seus respectivos preços na
#sequencia. No final, mostre uma listagem de preços, organizando os dados em for tabular
print('='*40)
print(f'{"Listagem de preços":^40}')
print('='*40)
listagem = ('Lápis', 1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
for c in range (0, 16,2):   
    print(f'{listagem[c]:.<30}',end='')
    print(f'R${listagem[c + 1]:>7.2f}')
    
    