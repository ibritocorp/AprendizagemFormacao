'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar e no final deve mostrar:

A) Qual é o total gasto na compra;
B) Quantos produtos custam mais de R$1.000;
C) Qual é o nome do produto mais barato.
'''

cabecalho = 'LOJA SUPER BARATÃO'
rodape = ' FIM DO PROGRAMA '

print('-' * 50)
print(f'{cabecalho:^50}')
print('-' * 50)

total = 0
contProdMaior = 0
prodBarato = ' '
menorVal = 0

while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$'))

    total += preco

    if preco > 1000:
        contProdMaior += 1
    
    if menorVal == 0:
        menorVal = preco
        prodBarato = produto
    
    if preco < menorVal:
        menorVal = preco
        prodBarato = produto

    continua = ' '
    while continua not in 'SN':
        continua = input('Quer continuar? [S/N] ').strip().upper()[0]
    
    if continua == 'N':
        break

print(f'{rodape:-^50}')
print(f'O total da compra foi R${total:.2f}')
print(f'Há {contProdMaior} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi o item "{prodBarato}" que custa R${menorVal:.2f}')
