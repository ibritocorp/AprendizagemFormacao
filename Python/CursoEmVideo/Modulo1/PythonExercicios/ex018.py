# Leia um ângulo qualquer e imprima na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

angulo = float(input('Digite o Ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem os seguintes valores trigonométricos:\nSENO: {seno:.2f}\nCOSSENO: {cosseno:.2f}\nTANGENTE: {tangente:.2f}')
