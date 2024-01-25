'''
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menos peso lidos.
'''

maiorPeso = 0
menorPeso = 1000

for i in range(0, 5):
    peso = float(input('Digite o peso: Kg'))
    if maiorPeso <= peso:
        maiorPeso = peso
    if menorPeso >= peso:
        menorPeso = peso

print(f'MENOR peso: Kg{menorPeso}\nMAIOR peso: Kg{maiorPeso}')
