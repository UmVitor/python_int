#Escreva um programa que leia a velocidade de um carro 
#se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar RS7,00 por cada km acima do limite

vel = int(input('Digite a velocidade do carro: '))
if (vel > 80):
    print('Você foi multado!!!!')
    print('Sua multa é de R${:.2f}'.format((vel-80)*7))
else:
    print('Você está dentro do limite permitido!!!')