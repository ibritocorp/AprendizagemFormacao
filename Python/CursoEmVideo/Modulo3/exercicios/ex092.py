'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho. Cadastre-os com idade em um dicionário e se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule a crescente, além da idade, com quantos anos a pessoa vai se aposentar (após 35 anos de contribuição).
'''

from datetime import datetime

pessoa = {}

pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['anocontrato'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['idadeaposenta'] = pessoa['idade'] - (datetime.now().year - pessoa['anocontrato']) + 35

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
