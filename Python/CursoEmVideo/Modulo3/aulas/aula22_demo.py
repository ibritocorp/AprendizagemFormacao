'''
from aula22 import fatorial, dobro, triplo
    Não recomendado, visto que ocorrerá conflito ao utilizar muitas bibliotecas e estas possuírem funções específicas com nomes iguais.
'''
import aula22
num = int(input("Digite um número inteiro: "))
print(f'O fatorial de {num} é {aula22.fatorial(num)}.')
print(f'O dobro de {num} é {aula22.dobro(num)}')
print(f'O triplo de {num} é {aula22.triplo(num)}')
