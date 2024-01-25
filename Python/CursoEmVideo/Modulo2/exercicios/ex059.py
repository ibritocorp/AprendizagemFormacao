'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

# Cabeçalho
print(f'{" CALCULADORA ":=^40}')

# Entrada dos números
num1 = float(input('Digite um número: ').strip())
num2 = float(input('Digite outro número: ').strip())

# Definição variável de resultado
resultado = 0

# Menu
print(f'{" MENU ":=^40}')
print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')

# Divisão gráfica menu
print(f'{"":=^40}')

# Entrada da opção
opcao = int(input('Digite a opção desejada: '))

# Execução
while opcao != 5:
    if opcao == 1:
        resultado = num1 + num2
    elif opcao == 2:
        resultado = num1 * num2
    elif opcao == 3:
        if num1 > num2:
            resultado = num1
        else:
            resultado = num2
    elif opcao == 4:
        # Nova entrada dos números
        num1 = float(input('Digite um número: ').strip())
        num2 = float(input('Digite outro número: ').strip())
    else:
        print('A opção digitada não é válida!')

    # Imprime o resultado
    print(f'O resultado desejado é {resultado}')

    # Menu
    print(f'{" MENU ":=^40}')
    print('''[1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')

    # Divisão gráfica menu
    print(f'{"":=^40}')

    # Entrada da opção
    opcao = int(input('Digite a opção desejada: '))

print('FIM')
