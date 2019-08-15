#Desenvolva um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preço da passagem. Cobrando RS0.50 por Km para viagens de até 200KM
#e RS0.45 para viagens mais longas

n1 = int(input('Digite a distancia da viagem: '))

if (n1 <= 200):
    tot = n1*0.5
    print('O preço da sua passagem é de R${:.2f}'.format(tot))
else:
    tot = n1*0.45 
    print('O preço da sua passagem é de R${:.2f}'.format(tot))