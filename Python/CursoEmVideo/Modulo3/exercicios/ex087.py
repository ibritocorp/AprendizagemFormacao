'''
Crie um programa que crie uma matriz de dimensão 3x3, preencha-a com valores lidos pelo teclado e no final mostre:

A) A soma de todos os números pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.
'''

# Declaração da lista composta
valores = [[],
           [],
           []]

# Declaração das variáveis simples
somapares = somaterceira = 0

# Laço de repetição para a leitura dos valores
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite um valor para [{x}, {y}]:'))
        valores[x].append(num)

        # Condicional para somar valores pares
        if num % 2 == 0:
            somapares += num

        # Condicional para somar os valores da terceira coluna
        if y == 2:
            somaterceira += num

# Formatação da saída no terminal
print('-=-' * 20)

# Laço de repetição para mostrar a matriz formatada
for linha in valores:
    for coluna in linha:
        # Mostrar os valores de cada item na formatação solicitada
        print(f'[ {coluna:^10} ]', end='')
    print()
        
# Formatação da saída no terminal
print('-=-' * 20)

# Mostrar a soma dos valores pares da matriz
print(f'A soma dos valores pares é {somapares}.')

# Mostrar a soma dos valores da terceira coluna
print(f'A soma dos valores da terceira coluna é {somaterceira}.')

# Mostrar o maior número da segunda linha
print(f'O maior valor da segunda linha é {max(valores[1])}')
