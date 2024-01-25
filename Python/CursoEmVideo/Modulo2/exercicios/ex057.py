'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação até ter um valor correto.
'''

sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('O valor digitado não corresponde ao padrão aceito. Digite "M" para Masculino ou "F" para Feminino: ').strip().upper()[0]

if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

print(f'Sexo {sexo} registrado com sucesso!')
