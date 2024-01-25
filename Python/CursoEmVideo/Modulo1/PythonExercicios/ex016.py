# Leia um número real qualquer e imprima na tela a sua parte inteira

# Solução simples sem a necessidade de importar uma biblioteca (módulo) ou função específica
'''n = float(input('Digite um número real com casas decimais: '))
print(f'O valor {n} possui a parte inteira {int(n)}.')'''

# Outra possibilidade de resolução simples
'''n = float(input('Digite um número real com casas decimais: '))
print(f'O valor {n} possui a parte inteira {n:.0f}.')'''

# Solução utilizando uma função específica de uma biblioteca (módulo)
from math import trunc

n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {trunc(n)}.')
