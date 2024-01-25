'''
Crie um programa que faça o computador jogar Jokenpô (Pedra, Papel e Tesoura) com você.
'''

from random import randint
from time import sleep

print(f'{" Jokenpô ":=^40}')

computador = randint(0, 2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

sleep(1)
print('JO')

sleep(1)
print('KEN')

sleep(1)
print('PO!!!')

sleep(1)
print('=' * 40)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {jogador}')
print('=' * 40)

if computador == jogador:
    print('EMPATE')
elif computador == 0 and jogador == 2:
    print('COMPUTADOR VENCE')
elif computador == 2 and jogador == 1:
    print('COMPUTADOR VENCE')
elif computador == 1 and jogador == 0:
    print('COMPUTADOR VENCE')
else:
    print('JOGADOR VENCE')