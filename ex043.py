#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule 
#seu IMC e mostre seu status, de acordo com a tabela abixo
#abaixo de 18.5 - Abaixo do peso
#Entre 18.5 e 25 - peso ideal
#Entre 25 e 30 - sobrepeso
#entre 30 ate 40 - obesidade
#Acima de 40 - obesidade morbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if(imc < 18.5):
    print('Abaixo do peso!!')
elif( 18.5<=imc<25):
    print('Peso ideal!!')
elif (25<=imc<30):
    print('Sobrepeso!!')
elif (30<=imc<40):
    print('Obesidade!!!')
else:
    print('Obesidade Mórbida')