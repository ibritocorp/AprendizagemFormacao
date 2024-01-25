'''
Crie um programa que vai ler vários números, colocá-los em uma lista e vai mostrar:

A) Quantos números foram digitados;
B) A lista de valores ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []
qtdVal = 0

while True:
    qtdVal += 1
    num = int(input('Digite um número inteiro qualquer: '))
    valores.append(num)
    continua = ' '
    while continua not in 'SN':
        continua = input('Deseja digitar mais um número? [S/N] ').strip().upper()[0]
    if continua == 'N':
        break

print(f'Foi/foram digitado(s) "{qtdVal}" valor(es).')

valores.sort(reverse=True)

print(f'Os valores em ordem decrescente são: {valores}')

if valores.count(5) >= 1:
    print('O número "5" está na lista.')
else:
    print('O número "5" não foi digitado.')
