#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
#Desconsiderando os espaços

word = input("Digite uma palara: ").strip()
word = word.replace(' ','')
word2 = word
tam = len(word)
aux = 0
for c in range (tam-1,-1,-1):
    if(word2[tam-c-1] != word[c]):
        aux = 1
if (aux == 0):
    print('PALINDROMO')
else:
    print('Não é palindromo')

