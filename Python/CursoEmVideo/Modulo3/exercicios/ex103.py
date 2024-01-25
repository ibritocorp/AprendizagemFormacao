'''
Faça um programa que tenha uma função "ficha()" que receba dois parâmetros opcionais, nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.
'''
# Função Printa Dados de Jogador
def ficha(nome = '<desconhecido>', gols = 0):
    print(f'{"-":-^60}')
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: ')).strip().title()
g = input('Número de Gols: ').strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)
