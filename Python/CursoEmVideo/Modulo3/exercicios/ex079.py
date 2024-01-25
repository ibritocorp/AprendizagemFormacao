'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. Os valores únicos devem ser exibidos em ordem crescente.
'''

valores = []

while True:
    num = int(input('Digite um número inteiro qualquer: '))

    if num not in valores:
        valores.append(num)

        continua = ' '
        while continua not in 'SN':
            continua = input('Deseja digitar mais um número? [S/N] ').strip().upper()[0]

        if continua == 'N':
            break
    else:
        print('Valor duplicado! Não será adicionado.')

print(f'Os valores digitados foram: {valores}')
print(f'Os valores em ordem crescente são: {sorted(valores)}')
