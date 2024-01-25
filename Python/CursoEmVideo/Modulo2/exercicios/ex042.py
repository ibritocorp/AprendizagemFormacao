"""
Refaça o exercício 035 acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados são iguais
- Idósceles: dois lados são iguais
- Escaleno: todos os lados são diferentes

Enunciado do exercício 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

reta1 = float(input('Digite o comprimento de uma reta: '))
reta2 = float(input('Digite o comprimento de outra reta: '))
reta3 = float(input('Digite o comprimento de outra reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'As retas PODEM formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO!')
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('As retas NÃO PODEM formar um triângulo!')
