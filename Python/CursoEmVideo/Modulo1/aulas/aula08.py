#Trabalhando com Módulos

# Na estrutura do Python existem bibliotecas, funções e módulos.
# Para importar uma biblioteca utilizamos o comando 'import + nome da bibilioteca + as + apelido'
# Para importar  'from + biblioteca + import + funcionalidade específica'
    # Exemplo:
    # import math ou import math as mt
    # from math import sqrt

import math
# from math import sqrt, ceil, floor
# Para não utilizar memória desnecessária a sugestão é importar as funções específicas como no exemplo da linha acima
num = float(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz}')

print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')
# Arredondar a raiz para cima

print(f'A raiz quadrada de {num} é {math.floor(raiz)}')
# Arredondar a raiz para baixo
