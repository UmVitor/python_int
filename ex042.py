#Diga se o triangulo é escaleno, isoceles ou equilatero. Em complemento a exercicios 35
import math
n1 = int(input('Digite um lado do triangulo: '))
n2 = int(input('Digite outro lado do triangulo: '))
n3 = int(input('Digite outro lado do triangulo: '))
if((n1 + n2) > n3 and (n2 + n3) > n1 and (n1 + n3)  > n2 and math.fabs(n1 - n2) < n3 and math.fabs(n3 - n2) < n1 and math.fabs(n3 - n1) < n2 ):
    print('Esse triangulo existe!!!')
    if(n1 == n2 == n3):
        print('Triangulo equilátero!!')
    elif(n1 != n2 != n3 != n1):
        print('Triangulo escaleno')
    else:
        print('Triangulo isóceles')
else:
    print('Esse triângulo não pode existir!!!')
