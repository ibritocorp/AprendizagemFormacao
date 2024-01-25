'''
Faça um programa que tenha uma lista chamada "numeros" e duas funções chamadas "sorteia()" e "somaPar()". A primeira função vai sortear 5 números e vai colocá-los dentro da lista, já a segunda vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''
from random import randint
from time import sleep


def sorteia(listnum):
    sleep(1)
    print('Sorteando 5 valores: ', end='', flush=True)
    for i in range(0, 5):
        listnum.append(randint(1, 10))
        sleep(0.5)
        print(listnum[i], end=' ', flush=True)
    print()


def somaPar(listnum):
    soma = 0
    sleep(1)
    print('Somando os valores pares: ', end='', flush=True)
    for v in listnum:
        if v % 2 == 0:
            soma += v
            sleep(0.5)
            print(v, end=' ', flush=True)
    print(f'=> A soma é: {soma}')
    print()


# Programa Principal
numeros = []
sorteia(numeros)
somaPar(numeros)
