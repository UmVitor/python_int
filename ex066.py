#Crie um programa que leia vários numeros inteiros pelo teclado. O programa
#só vai parar quando o usuário digitar o valor 9999, que é a condição de parada
#No final mostre quantos numeros foram digitados e qual foi a soma entre eles
#Obs: desconsiderando flag
s = count = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if (n == 999):
        break
    s += n
    count += 1
print(f'A soma dos {count} valores foi {s}!')