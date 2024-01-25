'''
Crie um programa que tenha uma função "fatoria()" que receba dois parâmetros:

1º - O número a calcular;
2º - Parâmetro chamado show que será o valor lógico (opicional) indicando se será mostrado ou não na tela o processo de cálculo.
'''
# Função p/ Calculo do Fatorial
def fatorial(num = 1, show = False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: Se o cálculo será mostrado ou não (False por padrão)
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    print(f'{"-":-^60}')
    for i in range(num, 0, -1):
        if show:
            print(f'{i}', end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    if show == False:
        print(f'O fatorial de {num} é: ', end='')
    return f


# Programa Principal
n = int(input('Digite o número inteiro que deseja o fatorial: '))
calc = ' '
while calc not in 'NS':
    calc = str(input('Deseja exibir o processo de cálculo [N-Não | S-Sim]? ')).strip().upper()[0]
if calc == 'S':
    mostra = True
else:
    mostra = False
print(fatorial(n, mostra))
