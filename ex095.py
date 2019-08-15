#Aprimore o desafio 93 para que ele funcione com varios jogadores, incluindo um 
#sistema de vizualização de detalhes de aproveitamento de cada jogador.
jogador = dict()
gols = list()
grupo = list()
soma = 0
sair = 'n'
while True:
    jogador["nome"] = str(input("Nome do jogador: "))
    jogador["partidas"] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0,jogador["partidas"]):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
        soma += gols[c]
    jogador['gols'] = gols[:]
    jogador['total'] = soma
    grupo.append(jogador.copy())
    gols.clear()
    soma = 0
    sair = str(input('Quer continuar? [S/N] '))
    print('-'*33)
    if (sair in 'Nn'):
        break    


print(f'{"Cod   "}{"nome":<10}{"gols":<10}{"total":^8}')
print('-'*33)

for c in range(0, len(grupo)):
    print(f'{c:<6}{grupo[c]["nome"]:<10}{grupo[c]["gols"]}{grupo[c]["total"]:>3}')

while True:
    print('-'*33)
    dados = int(input('Mostrar dados de qual jogador? '))
    if (dados > (len(grupo) - 1)):
       if(dados == 999):
           break
       else:
            print('Jogador inválido!!!! - Tente novamente.')                
            continue    
    print(f'levantamento do jogador {grupo[dados]["nome"]}')
    for c in range(0,grupo[dados]["partidas"]):
        print(" "*3,"=>",f'No jogo {c+1}, fez {grupo[dados]["gols"][c]} gols')
