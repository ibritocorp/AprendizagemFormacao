"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

# Estrutura de leitura dos valores
n1 = int(input('Digite um número inteiro: ').strip())
n2 = int(input('Digite outro número inteiro: ').strip())
n3 = int(input('Digite outro número inteiro: ').strip())

# Definição de um valor como menor para conferência, nesse caso o n1
menor = n1

# Estrutura condicional para comparação do menor valor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Definição de um valor como maior para conferência, nesse caso o n1
maior = n1

# Estrutura condicional para comparação do maior valor
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Estrutura para mostrar o resultado
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
