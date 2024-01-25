# Tipos primitivos e saída de dados

# int: números inteiros (7, -4, 0, 9875)
# float: números reais (4.5, 0.076, -15.223, 7.0)
# bool: valores lógicos ou booleanos (True ou False)
# str: strings ou caracteres (Olá, '7.5', '')

n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = n1 + n2
print(f'A soma vale {s}')
print(type(n1))
print(type(n2))
print(type(s))
# No exemplo acima, a função input não considera o número como tipo número, ele considera a entrada como string

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print(f'A soma vale {s}')
print(type(n1))
print(type(n2))
print(type(s))
# Nesse exemplo acima utilizamos o tipo primitivo 'int' (inteiro) para converter a string inserida em número
