'''
Um recurso possível é o uso do recurso fatiamento conforme exemplo abaixo.
'''

frase = input('Digite a frase: ').replace(' ', '')

if frase == frase[::-1]:
    print("A frase é um PALÍNDROMO.")
else:
    print('A frase NÃO É UM PALÍNDROMO.')
