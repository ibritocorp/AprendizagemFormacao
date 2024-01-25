i = 0

while True:
    i += 1
    print(f'{i}ª Passagem!')

    sair = ' '
    while sair not in 'sn':
        sair = input('Deseja finalizar? [S|N] ').strip().lower()[0]

    if sair == 's':
        break
