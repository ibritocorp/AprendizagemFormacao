'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

tupInt = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in tupInt:
    print(f'| {n} ', end='')
print('|')

print(f'O maior valor sorteado foi {max(tupInt)}')
print(f'O menor valor sorteado foi {min(tupInt)}')
