'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: ').strip())
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    print(f'Ainda vai se alistar. Falta(m) {18 - idade} ano(s) para o alistamento.')
elif idade > 18:
    print(f'Passou do tempo de alistamento. {idade - 18} ano(s) de atraso do alistamento.')
else:
    print('É hora de se alistar.')
