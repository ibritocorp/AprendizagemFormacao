'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se for ímpar, desconsidere-o.
'''

soma = 0

for cont in range(0, 6):
    n = int(input('Digite um número inteiro: ').strip())
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares digitados é: {soma}')
