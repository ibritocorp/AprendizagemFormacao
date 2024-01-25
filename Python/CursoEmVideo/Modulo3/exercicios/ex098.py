'''
Faça um programa que tenha uma função chamada "contador()" que receberá três parâmetros (inicio, fim e passo) e faça a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 a 10, de 1 em 1;
B) De 10 até 0, de 2 em 2;
C) Uma contagem personalizada.
'''
from time import sleep

def criaLinha():
    print(f'{"=":=^30}')


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    criaLinha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(1.5)
    if inicio <= fim:
        for i in range(inicio, fim + 1, passo):
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
        print()
    else:
        for f in range(inicio, fim - 1, passo * -1):
            print(f'{f}', end=' ', flush=True)
            sleep(0.5)
        print()


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
criaLinha()
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
