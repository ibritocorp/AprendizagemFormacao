"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

# Importação da função 'date' da biblioteca 'datetime'
from datetime import date

# Estrutura de leitura do ano
ano = int(input('Qual o ano deseja analisar? Digite "0" caso queira analisar o ano atual. ').strip())

# Estrutura condicional simples para verificar se é o ano atual através do valor digitado '0'
if ano == 0:
    ano = date.today().year

# Estrutura condicional composta para condição de bissexto
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')