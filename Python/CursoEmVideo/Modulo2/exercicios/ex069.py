'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos.
'''

cabecalho = 'CADASTRE UMA PESSOA'
rodape = ' FIM DO PROGRAMA '

maior = 0
homens = 0
mulheresMenor = 0

while True:
    print('-' * 50)
    print(f'{cabecalho:^50}')
    print('-' * 50)

    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    
    if idade > 18:
        maior += 1

    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulheresMenor += 1
    
    print('-' * 50)

    continua = ' '
    while continua not in 'SN':
        continua = input('Quer continuar? [S/N] ').strip().upper()[0]

    if continua == 'N':
        break

print(f'{rodape:=^50}')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheresMenor}')
