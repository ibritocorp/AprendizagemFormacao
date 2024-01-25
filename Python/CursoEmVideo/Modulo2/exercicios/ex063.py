'''
Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos de uma Sequênca de Fibonacci.

Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

n = int(input('Qual o número de elementos da Sequência de Fibonacci você deseja? '))

t1 = 0
t2 = 1
t3 = 1

i = 1

while i <= n:
    print(t3, end='')
    print(', ' if i < n else '', end='')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    i += 1
    