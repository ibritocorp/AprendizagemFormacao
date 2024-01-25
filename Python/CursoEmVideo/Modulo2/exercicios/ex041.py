'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima de 20 anos: MASTER
'''

from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Atleta MIRIM.')
elif 9 < idade <= 14:
    print('Atleta INFANTIL.')
elif 14 < idade <= 19:
    print('Atleta JUNIOR.')
elif 19 < idade <= 25:
    print('Atleta SÊNIOR.')
else:
    print('Atleta MASTER.')
