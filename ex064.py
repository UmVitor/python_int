#Crie um programa que leia vários número inteiros pelo teclado. O programa
#vai parar quandp o usuario digitar 999 que é a condição de parada
#Nofinal mostre quantos numeros foram digitados e qual foi a soma entre eles

flag = 0
cont = 0
soma = 0
while(flag != 999):
    flag = int(input('Digite um valor: '))
    if(flag != 999):
        soma += flag
        cont += 1
print('Foram digitados {} numeros!\n E a soma entre eles é: {}'.format(cont, soma))