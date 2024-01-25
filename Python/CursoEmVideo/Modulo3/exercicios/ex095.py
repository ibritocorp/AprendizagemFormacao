'''
Crie um programa que leia as seguintes informações:

* Nomes de jogadores;
* Quantas partidas os mesmos participaram;
* Quantidade de gols realizados por cada um em cada partida.

Os dados devem ser guardados em um dicionário, incluindo o total de gols feitos durante o campeonato.

Monte um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogador = {}
jogadores = []

print(f'{"-=-" * 20}\n{"DESEMPENHO DE JOGADORES":^60}\n{"-=-" * 20}')

while True:
    continua = ' '
    while continua not in 'NS':
        continua = str(input('Deseja preencher novo cadastro [N-Não / S-Sim]: ')).strip().upper()[0]
    if continua == 'N':
        break
    
    print(f'{"PREENCHA OS DADOS":-^60}')
    jogador['nome'] = str(input('Jogador: ')).strip().title()
    jogador['gols'] = []
    qtdpartidas = int(input('Partidas jogadas: '))
    for i in range(0, qtdpartidas):
        jogador['gols'].append(int(input(f'Gols realizados pelo {jogador["nome"]} na partida {i + 1}: ')))

    jogador['totgols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    print(f'{"-":-^60}')

print(f'{"-":-^60}')
print(f'{"Cód.":^15}{"Nome":^15}{"Gols":^15}{"Tot. Gols":^15}')
print(f'{"-":-^60}')

for k, v in enumerate(jogadores):
    print(f'{k:^15}', end='')
    for d in v.values():
        print(f'{str(d):^15}', end='')
    print()
print(f'{"-":-^60}')

while True:
    resp = str(input('Deseja detalhes de algum jogador [N-Não / S-Sim]? ')).strip().upper()[0]
    if resp not in 'NS':
        print('Digite [N] se NÃO quiser ver os detalhes e [S] para ver os detalhes de um jogador!')
    elif resp == 'N':
        break
    elif resp == 'S':
        codjogador = int(input('Digite o código do jogador que deseja ver os detalhes: '))
        print(f'{"-":-^60}')
        print(f'--Levantamento do jogador "{jogadores[codjogador]["nome"]}":')
        for ind, g in enumerate(jogadores[codjogador]["gols"]):
            print(f'No jogo {ind + 1} fez {g} gols.')
        print(f'{"-":-^60}')

print(f'{"SISTEMA ENCERRADO":-^60}')
