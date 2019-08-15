#Faça um programa que calcule a soma entre todos os numeros impares que são 
#multiplos de tres e que se encontram no intervalo de 1 ate 500
aux = 0
for c in range(1,501, 2):
##    aux = (2*c - 1)
    if(c%3 == 0):
        aux = aux + c
print('{}'.format(aux))