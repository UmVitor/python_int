#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
#cadastre-os(com idade) em um dicionario se por acaso a CTPS for diferente 
#de zero o funcionario receberá também o ano de contratação e  o salario
#Calcule e acrescente, além da idade, com quantos anos a pessoas vai se 
#aposentar. Considerando que a pessoas se aposente depois de 35 anos de colaboração

from datetime import date
ano_atual = date.today().year 
pessoas = dict()
pessoas["nome"] = str(input('Nome: '))
pessoas["idade"] = (ano_atual - int(input("Ano de nascimento: ")))
pessoas["ctps"] = (int(input("Carteira de trabalho (0 não tem): ")))
if(pessoas["ctps"] > 0):
    pessoas["contratação"] = int(input("Ano de contratação: "))
    pessoas["salário"] = float(input('Salário: '))
    pessoas["Aposentadoria"] = (35 - (ano_atual - pessoas["contratação"])) + pessoas["idade"]

print('-='*20)
for k, v in pessoas.items():
    print(f'{k} tem o valor {v}')


