lanches = ['Hambúrguer', 'Pizza', 'Salgado']
bebidas = ['Suco', 'Refrigerante', 'Água']

print(lanches)
print(bebidas)

cardapio = lanches + bebidas

print(cardapio)

cardapio.append('Biscoito')

print(f'{len(cardapio)} Ítens: {cardapio}')

cardapio.remove('Biscoito')

print(f'{len(cardapio)} Ítens: {cardapio}')

cardapio.pop()

print(f'{len(cardapio)} Ítens: {cardapio}')

crescente = list(range(10, 3, -2))

print(crescente)
