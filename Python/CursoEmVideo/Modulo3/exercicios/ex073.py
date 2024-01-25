'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação e depois mostre:

A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados da tabela;
C) Uma lista com os times em ordem alfabética;
D) Em que posição da tabela está o time Santos.
'''

classificacao = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')

prim = classificacao[:5]
ult = classificacao[-4:]

print(f'Os cinco primeiros colocados: {prim}')
print(f'Os quatro últimos colocados: {ult}')
print(f'Clubes em ordem alfabética: {sorted(classificacao)}')
print(f'O clube "Santos" está na {classificacao.index("Santos") + 1}º posição.')
