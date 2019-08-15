#Faca um programa que leia uma frase pelo teclado e mostre
#Quantas vezes aparece a letra 'a'
#em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).lower().strip()
print(frase)
print('Nesta frase a letra a aparece {} vezes!'.format(frase.count('a')))
print('A letra A aparece {} vezes!'.format(frase.count('a')))
print('A primeira ocorrencia dessa letra é na {}° posição'.format(frase.find('a')+1))
print('A ultima ocorrencia dessa letra é na {}° posição'.format(frase.rfind('a')+1))