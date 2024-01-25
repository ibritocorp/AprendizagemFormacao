primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + 1, razao):
    print(f'{i}', end=' -> ')
print('ACABOU!')
