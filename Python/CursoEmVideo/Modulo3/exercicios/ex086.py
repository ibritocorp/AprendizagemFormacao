'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela com a formatação correta.
'''

# Declaração da lista composta
valores = [[],
           [],
           []]

# Laço de repetição para a leitura dos valores
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]:'))
        valores[linha].append(num)

# Formatação da saída no terminal
print('-=-' * 20)

# Mostrar os valores das sublistas
for val in valores:
    print(val)

# Formatação da saída no terminal
print('-=-' * 20)

# Mostrar os valores de cada item na formatação de matriz
for v in valores:
    for i in v:
        print(f'[ {i:^10} ]', end='')
    print()
