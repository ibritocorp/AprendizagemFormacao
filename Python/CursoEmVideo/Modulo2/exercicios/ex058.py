'''
Melhore o jogo do exercício 028, porém considerando de 0 até 10. Agora você vai tentar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep

# Faz o computador sortear um número entre 0 e 10
computador = randint(0, 10)

# Monta um cabeçalho para uma estética melhor
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

# Define variável vazia
jogador = int(input('Em qual número eu pensei? ').strip())

# Inicializa contador
cont = 1

# Verifica as condições
while jogador != computador:
    jogador = int(input('Não foi o número que pensei! Vamos lá, qual número eu pensei? ').strip())
    cont += 1

# Processa e impime na tela o resultado
print('PROCESSANDO...')
sleep(2)

print(f'Foi(ram) necessário(s) {cont} palpite(s) para acertar o número {computador}!')
