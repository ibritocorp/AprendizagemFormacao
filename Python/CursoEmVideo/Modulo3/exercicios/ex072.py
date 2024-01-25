'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e vinte) e mostrá-lo por extenso.
'''

nExtenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

#while True:
#    num = int(input('Digite um número entre 0 e 20 para ver sua escrita por extenso: '))
#    if 0 <= num <= 20:
#        break

num = ' '
while num not in range(0, 21):
    num = int(input('Digite um número entre 0 e 20 para ver sua escrita por extenso: '))

print(f'O número {num} em extenso é "{nExtenso[num]}".')
