#Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato
#Brasileiro de Futebol, na ordem de colocação. Depois mostre.
#A)Apesar os 5 primeiros colocados
#B)Os últimos 4 colocados da tabela 
#C) Uma lista com os times em ordem alfabetica 
#D) Em que posição na tabela está o time da chapecoense

brasileirao = ('Palmeiras' , 'Santos' , 'Flamengo','Internacional', 'Atlético-MG','Goiás','Botafogo','Bahia','São Paulo','Corinthians','Grêmio','Athletico-PR','Ceará','Fortaleza','Vasco','Fluminense','Chapecoense','Cruzeiro','CSA','Avaí')
print(f'Lista de times do Brasileirão: {brasileirao}')
print(f'Os 5 primeiros são {brasileirao[:5]}')
print(f'Os 4 ultimos são {brasileirao[-5:]}')
print(f'Os times em ordem alfabetica são {sorted(brasileirao)}')
print('O time da Chapecoense está na {}° posição'.format(brasileirao.index('Chapecoense') + 1))
