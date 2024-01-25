'''
Crie um programa que leia nome, duas notas e guarde tudo em uma lista composta. Calcule a média e acrescente na lista, após isso mostre o nome, as notas e a média de cada aluno.
'''

from time import sleep

fichasalunos = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    fichasalunos.append([nome, [nota1, nota2, media]])
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print(f'{"-":-^38}')
print(f'{"|"}{"ID":^10}{"|":^3}{"NOME":^10}{"|":^3}{"MÉDIA":^10}{"|"}')
print(f'{"-":-^38}')

for i, n in enumerate(fichasalunos):
    print(f'{"|"}{i:^10}{"|":^3}{n[0]:^10}{"|":^3}{n[1][2]:^10}{"|"}')

print(f'{"-":-^38}')

while True:
    vernotas = ' '
    while vernotas not in 'SN':
        vernotas = str(input('Deseja ver as notas detalhadas? [S/N] ')).strip().upper()[0]
    if vernotas == 'N':
        break

    id = int(input('Mostrar notas de qual aluno? '))
    print(f'{"-":-^64}')
    print(f'{"|"}{"ID":^10}{"|":^3}{"NOME":^10}{"|":^3}{"NOTA 1":^10}{"|":^3}{"NOTA 2":^10}{"|":^3}{"MÉDIA":^10}{"|"}')
    print(f'{"-":-^64}')
    print(f'{"|"}{id:^10}{"|":^3}{fichasalunos[id][0]:^10}{"|":^3}{fichasalunos[id][1][0]:^10}{"|":^3}{fichasalunos[id][1][1]:^10}{"|":^3}{fichasalunos[id][1][2]:^10}{"|"}')
    print(f'{"-":-^64}')

print(f'{"VOLTE SEMPRE":-^64}')
