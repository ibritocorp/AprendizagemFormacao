# Leia quatro nomes, sorteie aleatoriamente a ordem de apresentação desses alunos

from random import sample, shuffle

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')

# Uma solução possível
lista = [nome1, nome2, nome3, nome4]
print(lista)
print(f'A ordem de apresentação será: {shuffle(lista)}')

# Outra solução possível
print(f'A ordem de apresentação será: {sample([nome1, nome2, nome3, nome4], k=4)}')
