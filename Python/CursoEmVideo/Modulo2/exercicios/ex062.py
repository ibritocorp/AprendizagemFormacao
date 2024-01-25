primeiro = i = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
cont = 0
opcao = ''

while opcao != 'N':
    while i <= decimo:
        print(f'{i}', end='')
        print(' -> ' if i < decimo else '', end='')
        i += razao
        cont += 1
    opcao = input('\nQuer mostrar mais termos? [S/N] ').strip().upper()[0]
    if opcao == 'S':
        termo = int(input('Quantos? '))
        decimo = i + (termo - 1) * razao
print(f'Progressão finalizada com {cont} termos mostrados.')
