"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Condições:

* Para salários superiores a R$1.250,00, calcule um aumento de 10%.
* Para salários inferiores ou iguais o aumento é de 15%
"""

salarioAtual = float(input('Digite o salário: R$').strip())
if salarioAtual >= 1250:
    salarioReajustado = salarioAtual + (salarioAtual * 0.1)
else:
    salarioReajustado = salarioAtual + (salarioAtual * 0.15)
print(f'O salário reajustado é R${salarioReajustado:.2f}')