primeiro = i = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

while i <= decimo:
    print(f'{i}', end='')
    print(' -> ' if i < decimo else '', end='')
    i += razao
