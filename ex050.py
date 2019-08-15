#desenvolva um programa que leia seis numeor inteiros e mostre a soma apenas 
#daqueles que forem pares. Se o valor digitado for impar desconsidere
aux2 = 0
for c in range(1,7):
    aux = int(input('Digite um numero: '))
    if(aux%2 == 0):
        aux2 += aux
print(aux2)
