'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print(f'{"=":=^50}\n{"BANCO CEV":^50}\n{"=":=^50}')

valSaque = int(input('Que valor você quer sacar? R$'))
total = valSaque
valCedula = 50
totalCedula = 0

while True:
    if total >= valCedula:
        total -= valCedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${valCedula}')
        
        if valCedula == 50:
            valCedula = 20
        elif valCedula == 20:
            valCedula = 10
        elif valCedula == 10:
            valCedula = 1
        
        totalCedula = 0

        if total == 0:
            break

print(f'{"=":=^50}\n{"Volte sempre ao BANCO CEV!":^50}')
