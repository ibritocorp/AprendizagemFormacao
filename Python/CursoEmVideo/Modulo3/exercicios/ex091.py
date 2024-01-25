'''
Crie um pograma onde 4 jogogadores joguem um dado, tenham resultados aleatórios e guarde-os em um dicionário. Ao final, coloque o dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from time import sleep
from random import randint

jogadas = []
jogador = {}

for i in range(0, 4):
    jogador['nome'] = 'jogador' + str(i + 1)
    jogador['numero'] = randint(1, 6)
    jogadas.append(jogador.copy())

jogadas_ordenadas = sorted(jogadas, key=lambda k: k['numero'], reverse=True)

print('Valores sorteados:')

for j in jogadas:
    sleep(1)
    print(f'O {j["nome"]} tirou {j["numero"]}')

sleep(1)
print('Ranking dos jogadores:')

for rank, j in enumerate(jogadas_ordenadas, start=1):
    sleep(1)
    print(f'{rank}º lugar: {j["nome"]} - {j["numero"]}')
