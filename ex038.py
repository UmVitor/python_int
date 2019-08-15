#Escreva um programa que leia dois numeros inteiros e compare-os mostrando
#na tela uma mensagem.
#O primeiro valor é maior
#o segundo valor é maior 
#não existe valor maior, os dois são iguais
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

if (n1 > n2):
    print('O primeiro valor é maior')
elif (n1 < n2):
    print('O segundo valor é maior')
else:
    print('não existe valor maior, os dois são iguais')