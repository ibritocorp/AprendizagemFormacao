"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# Meu código

"""
from random import randrange

nAleatorio = randrange(0, 6)
nDigitado = int(input('Digite o número de 1 a 5: ').strip())
if nAleatorio == nDigitado:
    print('Você venceu!')
else:
    print('Você perdeu!')
print(f'O número escolhido pelo computador foi {nAleatorio} e o que digitou foi {nDigitado}')
"""

# Código corrigido

from random import randint
from time import sleep

# Faz o computador sortear um número entre 0 e 5
computador = randint(0, 5)

# Monta um cabeçalho para uma estética melhor
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

# Pede ao jogador para tentar advinhar o número
jogador = int(input('Em que número eu pensei? ').strip())
print('PROCESSANDO...')
sleep(2)

# Verifica as condições
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
