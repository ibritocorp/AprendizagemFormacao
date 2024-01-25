'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador, quantas partidas ele jogou e a quantidade de gols em cada partida. Todas as informações devem ser guardadas em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = {}
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
jogador['gols'] = []
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
totgols = 0
if partidas > 0:
    for i in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))

jogador['totgols'] = sum(jogador['gols'])

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partida(s).')

for i, g in enumerate(jogador['gols']):
    print(f'=> Na partida {i + 1}, fez {g} gol(s).')

print(f'Foi um total de {jogador["totgols"]}')
