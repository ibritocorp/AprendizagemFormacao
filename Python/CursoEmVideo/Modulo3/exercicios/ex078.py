'''
Faça um programa que leia 5 valores, guarde-os em uma lista e ao final mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
'''

valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor inteiro qualquer para a posição {i}: ')))

print(f'O maior valor digitado foi "{max(valores)}" e está na posição "{valores.index(max(valores))}".')
print(f'O menor valor digitado foi "{min(valores)}" e está na posição "{valores.index(min(valores))}".')
