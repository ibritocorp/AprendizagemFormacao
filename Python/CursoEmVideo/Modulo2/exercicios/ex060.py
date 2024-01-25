'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

n = cont = fatorial = int(input('Digite um número: ').strip())

while cont != 1:
    print(f'{cont} x ', end='')
    cont -= 1
    fatorial = fatorial * cont

print(f'1\nO fatorial de {n} é: {fatorial}')
