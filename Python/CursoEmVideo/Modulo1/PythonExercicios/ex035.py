"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

# Meu código

"""
# Leitura dos valores por digitação do teclado
reta1 = float(input('Digite o comprimento de uma reta: '))
reta2 = float(input('Digite o comprimento de outra reta: '))
reta3 = float(input('Digite o comprimento de outra reta: '))

# Estrutura para calcular o menor valor
menor = reta1
if reta2 < reta1 and reta2 < reta3:
    menor = reta2
if reta3 < reta1 and reta3 < reta2:
    menor = reta3

# Estrutura para calcular o maior valor
maior = reta1
if reta2 > reta1 and reta2 > reta3:
    maior = reta2
if reta3 > reta1 and reta3 > reta2:
    maior = reta3

# Estrutura para calcular o valor do meio
if reta1 > reta2 and reta1 < reta3 or reta1 < reta2 and reta1 > reta3:
    meio = reta1
elif reta2 > reta1 and reta2 < reta3 or reta2 < reta1 and reta2 > reta3:
    meio = reta2
else:
    meio = reta3

# Estrutura para verificar se as retas formam um triângulo
if (maior - meio) < menor and menor < (maior + meio):
    tst1 = True
else:
    tst1 = False

if (meio - menor) < maior and maior < (meio + menor):
    tst2 = True
else:
    tst2 = False

if (maior - menor) < meio and menor < (maior + menor):
    tst3 = True
else:
    tst3 = False

# Mostrar resultado
if tst1 == True and tst2 == True and tst3 == True:
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo.')
"""

# Código corrigido

# Leitura dos valores por digitação do teclado
reta1 = float(input('Digite o comprimento de uma reta: '))
reta2 = float(input('Digite o comprimento de outra reta: '))
reta3 = float(input('Digite o comprimento de outra reta: '))

# Condicional para verificar se as retas podem formar o triângulo
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas PODEM formar um triângulo!')
else:
    print('As retas NÃO PODEM formar um triângulo!')
