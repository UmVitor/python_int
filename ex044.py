#Elabore um programa que calcule o valor a ser pago por um produto, considerando
#o seu preço normal e condição de pagamento.
#A vista dinheiro/cheque 10% de desconto
#A vista no cartão 5% de desconto
#em ate 2x no cartao - preço normal 
#3x ou mais no cartão 20% de juros

preco = float(input('Insira o preço do produto: '))
pag = int(input('Digite a opção de pagamento\n 1-A vista dinheiro/cheque 10% de desconto\n 2-A vista no cartão 5% de desconto\n 3-em ate 2x no cartao - preço normal\n 4-3x ou mais no cartão 20% de juros: '))

if (pag == 1):
    print(preco*0.9)
elif(pag == 2):
    print(preco*0.95)
elif(pag == 3):
    print(preco)
elif(pag == 4):
    print(preco)
else:
    print('Opção invalida!!!!')