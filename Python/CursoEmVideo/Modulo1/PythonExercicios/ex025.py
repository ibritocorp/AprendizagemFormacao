"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
"""

nome = input('Digite o nome: ').strip()
print('Analisando se o nome possui SILVA...')
print('silva' in nome.lower())
