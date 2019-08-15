#Faça um programa que tenha uma função chamada escreva() que receba um texto
#qualquer como parâmetro e mostre uma mensagem com tamanho adaptavel

def escreva(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'{"  "}{msg}{"  "}')
    print('-'*tam)

k = "Neuron to brain"
k1 = "Vitor Barreto Souza"
escreva(k)
escreva(k1)