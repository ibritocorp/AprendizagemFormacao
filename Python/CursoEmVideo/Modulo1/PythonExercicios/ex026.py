"""
Crie um programa que leia uma frase e mostre:

* Quantas vezes aparece a letra 'A'
* Em que posição ela aparece pela primeira vez
* Em que posição ela aparece a última vez
"""

frase = input('Digite uma frase: ').lower().strip()
print(f'Analisando a frase "{frase}"...')
print(f'A letra "a" aparece {frase.count("a")} vez(es).')
print(f'A primeira letra "a" aparece na posição {frase.find("a") + 1}.')
print(f'A última letra "a" aparece na posição {frase.rfind("a") + 1}')
