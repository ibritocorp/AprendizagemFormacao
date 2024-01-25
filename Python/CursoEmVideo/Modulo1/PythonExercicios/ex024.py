"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
"""

cidade = input('Digite o nome da cidade: ').strip()
print('Analisando se a cidade começa pela palavra SANTO...')
separa = cidade.lower().split()
print('santo' in separa[0])
