'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print(len(frase))
print(frase.lower())
print(frase.lower()[::-1])
'''

frase = input('Digite a frase: ').replace(' ', '')
fraseCompara = ''

for i in range(len(frase) - 1, -1, -1):
    fraseCompara += frase[i]

if frase == fraseCompara:
    print("A frase é um PALÍNDROMO.")
else:
    print('A frase NÃO É UM PALÍNDROMO.')
