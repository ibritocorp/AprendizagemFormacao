# Leia quatro nomes e sorteie aleatoriamente um desses nomes

from random import choice

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
print(f'Esse(a) foi o(a) escolhido(a): {choice([nome1, nome2, nome3, nome4])}')
