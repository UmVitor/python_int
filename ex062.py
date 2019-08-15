#Melhore o program o61, perguntado para o usuario se ele quer mostrar mais 
#termos. O programa encerra quando ele disser que quer mostrar 0 termos

a1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
sair = 1
count = 0
count2 = 10
while(sair !=  0):
    print(a1)
    a1 = a1 + r
    count += 1
    if(count == count2):
        sair = int(input('Você quer mostrar mais quantos termos? '))
        count = 0
        count2 = sair

