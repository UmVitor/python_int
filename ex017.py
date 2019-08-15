#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulp retangulo, calcule e mostre o comprimento da hipotenusa

import math
cad = float(input('Insira o cateto adjacente: '))
cop = float(input('Insira o cateto oposto: '))
hip = math.sqrt(math.pow(cad,2)  + math.pow(cop,2))
print('A hipotenusa vale: {}'.format(hip))