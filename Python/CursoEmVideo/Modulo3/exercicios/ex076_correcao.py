'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

print(f'{"=":=^50}\n{"LISTAGEM DE PREÇOS":^50}\n{"=":=^50}')

lista = ('Lápis', 0.85, 'Caneta', 1.2, 'Borracha', 1.5, 'Caderno', 3)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<40}R$', end='')
    else:
        print(f'{lista[i]:>8.2f}')

print(f'{"=":=^50}')
