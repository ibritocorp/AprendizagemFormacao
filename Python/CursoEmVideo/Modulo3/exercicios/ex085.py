'''
Crie um programa onde o usuário possa digitar sete valores numéricos, cadastre-os em uma lista única que mantenha separados os valores pares e ímpares, e no final mostre os valores pares e ímpares em ordem crescente.
'''

# Declaração de lista composta
valores = [[], []]

# Laço de repetição para recebimento dos valores
for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}º valor: '))
    
    # Estrutura condicional para apontamento correto na lista composta
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

# Método para ordenar em ordem crescente
valores[0].sort()
valores[1].sort()

# Cabeçalho
print('-=-' * 20)

# Mostrar listas pares e ímpares ordenadas
print(f'Os valores PARES digitados foram: {valores[0]}')
print(f'Os valores ÍMPARES digitados foram: {valores[1]}')
