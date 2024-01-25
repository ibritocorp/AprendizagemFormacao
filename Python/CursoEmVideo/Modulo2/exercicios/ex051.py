'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
'''

priTermo = int(input('Digite o primeiro termo de uma Progressão Aritmética: ').strip())
razao = int(input('Digite a razão de uma Progressão Aritmética: ').strip())
n = priTermo

for cont in range(0, 10):
    print(f'{n} {"-> "}', end='')
    n += razao
print('FIM')
