#Faça um programa que tenha uma função chamada área(), que receba as 
#dimmensões de um terreno retangular (largura e comprimento) e mostre
#a área do terreno

def area():
    area = larg*comp
    print(f'Area de um terreno {larg} X {comp} é de {area}m².')


print('Controle de Terrenos')
larg = float(input('Largura(m): '))
comp = float(input('Comprimeto(m): '))
area()