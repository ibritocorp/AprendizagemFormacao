'''
1) Crie um módulo chamado "moeda.py" que tenha funções incorporadas "aumentar()", diminuir(), dobro() e metade().

2) Faça um programa que importe esse módulo e use algumas dessas funções.
'''
from ex107 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor)}')
print(f'Diminuindo 13%, temos R${moeda.diminuir(valor)}')
