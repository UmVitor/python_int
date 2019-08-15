#Crie um programa onde o usuário digite uma expressão qualquer que use
#parenteses. Seu aplicativo deverá analisar se a expressão passada está
#com parentesis abertos e fechados na ordem correta

n = []
n.append(str(input('Digite sua expressão: ')))
if (n.count('(') == n.count(')')):
    print('Sua expressão está correta!!')
else:   
    print('Sua expressão está errada!!!')
