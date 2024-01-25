lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for alimento in lanche[1:]:
    print(alimento)

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, alimento in enumerate(lanche):
    print(f'{alimento} está na posição {pos}.')
