#Faça um programa que mostre a tabuada de varios numeros, um de cada vez
# para cada valor digitado pelo usuario. O programa será interrompido quando
#o número solicitado for negativo

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if (n < 0 ):
        break
    print('-'*20)
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-'*20)