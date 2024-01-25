'''
Crie um programa que vai ler vários números, colocar em uma lista e seguir as instruções abaixo:

A) Criar uma nova lista com os valores pares digitados;
B) Criar uma nova lista com os valores ímpares digitados;
C) Exibir as três listas.
'''

valores = []
pares = []
impares = []

while True:
    num = int(input('Digite um valor inteiro qualquer: '))
    valores.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    continua = ' '
    while continua not in 'SN':
        continua = input('Digite "S" para inserir um novo valor ou "N" para finalizar: ').strip().upper()[0]

    if continua == 'N':
        break

print(f'Os valores digitados foram: {valores}')

if len(pares) == 0:
    print('Não foi digitado número PAR!')
elif len(pares) == 1:
    print(f'O número PAR digitado foi: {pares}')
else:
    print(f'Os números pares digitados foram: {pares}')

if len(impares) == 0:
    print('Não foi digitado número ÍMPAR!')
elif len(impares) == 1:
    print(f'O número ÍMPAR digitado foi: {impares}')
else:
    print(f'Os números ímpares digitados foram: {impares}')
