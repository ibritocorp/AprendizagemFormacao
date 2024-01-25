'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date

contMaiorIdade = 0
contMenorIdade = 0

for i in range(0, 7):
    anoNascimento = int(input('Digite o ano de nascimento: ').strip())
    if date.today().year - anoNascimento >= 21:
        contMaiorIdade += 1
    else:
        contMenorIdade += 1

print(f'{contMaiorIdade} pessoas atingiram a MAIOR IDADE e {contMenorIdade} ainda NÃO ATINGIRAM A MAIOR IDADE!')
