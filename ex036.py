#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos 
#anos ele vai pagar.
#OBS:Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% 
#salário ou então o emprestimo será negado.

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos você deseja quitar: '))
prestacao = casa/(anos*12)
if (prestacao > salario*0.3):
    print('Emprestimo Negado!!!!')
elif (prestacao == salario*0.3):
    print('Emprestimo aprovado com limite de cota!!!!!\n suas parcelas são de R${:.2f}'.format(prestacao))
else:
    print('Empréstimo aprovado\n suas parcelas são de R${:.2f}'.format(prestacao))