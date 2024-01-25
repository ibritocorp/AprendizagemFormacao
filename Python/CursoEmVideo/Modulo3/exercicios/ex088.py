'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta.
'''

# Importa biblioteca random
from random import sample

# Importa método sleep da biblioteca time
from time import sleep

# Cria lista
palpites = []

# Formata cabeçalho
print(f'{"=":=^50}\n{"JOGA NA MEGA SENA":^50}\n{"=":=^50}')

# Pergunta a quantidade de palpites desejados
qtdpalpites = int(input('Quantos jogos você quer que eu sorteie? '))

# Laço de repetição para sortear os número aleatórios e adicionar na lista
for p in range(qtdpalpites):
    palpite = sample(range(1, 61), 6)
    palpite.sort()
    palpites.append(palpite)

# Pausa
sleep(1)

# Formata continuidade
print(f'{"=":=^50}\n{"SORTEANDO":^50}\n{"=":=^50}')

# Laço de repetição para formatar e apresentar sublistas
for i, jogo in enumerate(palpites):
    sleep(1)
    print(f'Jogo {i + 1}: {jogo}')
    print(f'{"=":=^50}')
