maior = 0
menor = 0

for i in range (0, 5):
    peso = float(input(f'Peso da {i + 1}ª pessoa: Kg'))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior} Kg.')
print(f'O menor peso lido foi de {menor} Kg.')
