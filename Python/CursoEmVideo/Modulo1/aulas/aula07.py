# Operadores aritméticos

# Operador '+': Adição
5 + 2 == 7

# Operador '-': Subtração
5 - 2 == 3

# Operador '*': Multiplicação
5 * 2 == 10

# Operador '/': Divisão
5 / 2 == 2.5

# Operador '**': Potência
5 ** 2 == 25

# Operador '//': Divisão inteira
5 // 2 == 2

# Operador '%': Resto da divisão (módulo)
5 % 2 == 1

#Ordem de precedência
# Conchetes e chaves são utilizados para outras coisas
# 1º: () - Parênteses podem estar dentro de parênteses mudando a ordem de dentro para fora
# 2º: **
# 3º: *, /, //, %
# 4º: +, -

5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243

# Outras considerações
# Função de potência 'pow()'
4 ** 3 == 64
pow (4,3) == 64

# Raiz quadrada é o mesmo que número potenciação '1/2' ou '0.5'
81 ** (1/2) == 9.0
81 ** 0.5 == 9.0

# Raiz cúbica é o mesmo que número potenciação '1/3'
343 ** (1/3) == 7.0

# Operadores c/ string
'Oi' + 'Olá' == 'OiOlá'
'Oi' * 5 == 'OiOiOiOiOi'
'=' * 20 == '===================='

# Formatação e função print
nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome:20}!')
# Formatação '{nome:20}': Variável em 20 espaços

print(f'Prazer em te conhecer, {nome:>20}!')
# Formatação '{nome:>20}': Variável em 20 espaços alinhado à direita

print(f'Prazer em te conhecer, {nome:^20}!')
# Formatação '{nome:^20}': Variável em 20 espaços alinhado centralizado

print(f'Prazer em te conhecer, {nome:*^20}!')
# Formatação '{nome:*^20}': Variável em 20 espaços alinhado centralizado com o preenchimento do caractere inserido após ':'

