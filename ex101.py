#Crie um programa que tenha uma função chamada voto() que vai receber como
#parametro o ano de nascimento de uma pessoa, retornando um valor literal
#indicando se uma pessoa tem voto Negado, opcional ou obrigatorio

from datetime import date

def voto(i):
    n1 = date.today().year
    idade = n1 - i
    
    if(idade < 16):
        return f'Você tem: {idade} anos.\nVOTO NEGADO!!'
    elif((16 < idade < 18) or (idade>60)):
        return f'Você tem: {idade} anos.\nVOTO FACULTATIVO!!'
    else:
        return f'Você tem: {idade} anos.\nVOTO OBRIGATORIO!!!'


a = int(input('Data de nascimento: '))
print(voto(a))