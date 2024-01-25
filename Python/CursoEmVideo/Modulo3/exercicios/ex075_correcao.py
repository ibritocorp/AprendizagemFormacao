'''
Desenvolva um programa que leia quatro valores pelo teclado, guarde-os em uma tupla e no final mostre:

A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
C) Quais foram os números pares.
'''

valores = (int(input('Insira um valor: ')), int(input('Insira um valor: ')), int(input('Insira um valor: ')), int(input('Insira um valor: ')))

print(f'Você digitou os valores {valores}')

print(f'O valor "9" foi digitado {valores.count(9)} vez(es).')

if 3 in valores:
    print(f'O valor "3" foi digitado na {valores.index(3) + 1}ª posição.')
else:
    print('O valor "3" não foi digitado.')

print('Os valores pares digitados foi/foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
