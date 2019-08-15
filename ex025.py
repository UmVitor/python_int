#Crie um progrma que leia ao nome de uma pessoa e diga se ela te 'Silva' no nome

nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome possui Silva? {}!'.format('silva' in nome.lower()))