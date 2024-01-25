'''
Faça um programa que tenha uma função chamada area(), receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área desse terreno.
'''
# Função Cabeçalho
def cabecalho(tam, titulo):
    print(f'{"-":-^{tam}}\n{titulo:^{tam}}\n{"-":-^{tam}}')


# Função area()
def area(b, h):
    a = b * h
    print(f'A área de um terreno {b} x {h} é de {a:.2f} m².')


# Programa Principal
cabecalho(40, 'MEDE TERRENO')
larg = float(input('Metragem do Comprimento: '))
comp = float(input('Metragem da Largura: '))
area(comp, larg)
