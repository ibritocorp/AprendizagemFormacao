# Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# Solução simples sem uso de funções específicas e bibliotecas (módulos)
'''catOposto = float(input('Digite o comprimento do Cateto Oposto: '))
catAdjacente = float(input('Digite o comprimento do Cateto Adjacente: '))
hipotenusa = (catOposto ** 2 + catAdjacente ** 2) ** 1/2
print(f'A hipotenusa mede {hipotenusa:.2f}')'''

# Solução com o uso de funções específicas de uma biblioteca (módulo)
'''from math import pow, sqrt

catOposto = float(input('Digite o comprimento do Cateto Oposto: '))
catAdjacente = float(input('Digite o comprimento do Cateto Adjacente: '))
hipotenusa = sqrt(pow(catOposto, 2) + pow(catAdjacente, 2))
print(f'A hipotenusa mede {hipotenusa:.2f}')'''

# Solução mais compacta com o uso de função específica de uma biblioteca (módulo)
from math import hypot

catOposto = float(input('Digite o comprimento do Cateto Oposto: '))
catAdjacente = float(input('Digite o comprimento do Cateto Adjacente: '))
hipotenusa = hypot(catOposto, catAdjacente)
print(f'A hipotenusa mede {hipotenusa:.2f}')