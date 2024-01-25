from random import randint
from time import sleep

print(f'{" Jokenpô ":=^40}')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PÔ!!!')
sleep(1)

print('=' * 40)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print('=' * 40)

if computador == 0: # Computador jogou Pedra
    if jogador == 0: # Jogador jogou Pedra
        print('EMPATE')
    elif jogador == 1: # Jogador jogou Papel
        print('JOGADOR VENCE')
    elif jogador == 2: # Jogador jogou Tesoura
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 1: # Computador jogou Papel
    if jogador == 0: # Jogador jogou Pedra
        print('COMPUTADOR VENCE')
    elif jogador == 1: # Jogador jogou Papel
        print('EMPATE')
    elif jogador == 2: # Jogador jogou Tesoura
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 2: # Computador jogou Tesoura
    if jogador == 0: # Jogador jogou Pedra
        print('JOGADOR VENCE')
    elif jogador == 1: # Jogador jogou Papel
        print('COMPUTADOR VENCE')
    elif jogador == 2: # Jogador jogou Tesoura
        print('EMPATE')
    else:
        print('Jogada inválida!')
