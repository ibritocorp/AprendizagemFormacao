'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário e ao final mostre o conteúdo da estrutura na tela.

Média >= 7 - Aprovado
Média <= 7 - Reprovado
'''

aluno = {'nome': str(input('Nome: ')).strip(), 'media': float(input('Média: '))}

if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')
