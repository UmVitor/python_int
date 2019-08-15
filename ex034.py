#Escreva um programa que pergunte o salário de um funicionario e calcule o valor
#do seu aumento, para salários superiores a RS1.250,00 calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salario: '))
if(salario > 1250):
    print('O novo salário será de R${:.2f}'.format(salario*1.1))
else:
    print('O novo salário será de R${:.2f}'.format(salario*1.15))