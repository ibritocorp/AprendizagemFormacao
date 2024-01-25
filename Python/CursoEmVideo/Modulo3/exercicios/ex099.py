'''
Faça um programa que tenha uma função chamada "maior()" que receba vários valores inteiros por parâmetro e diga qual deles é o maior.
'''
from time import sleep


def criaLinha():
    print(f'{"=":=^30}')


def maior(* numeros):
    criaLinha()
    print('Analisando', end='', flush=True)
    for i in range(0, 5):
        sleep(0.5)
        print('.', end='', flush=True)
    print()
    criaLinha()
    sleep(0.5)
    print(f'{len(numeros)} analisado(s):')
    for n in numeros:
        sleep(0.5)
        print(n, end=' ', flush=True)
    print()
    print(f'O maior valor foi {max(numeros)}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
