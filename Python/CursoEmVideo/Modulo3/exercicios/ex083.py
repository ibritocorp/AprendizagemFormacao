'''
Crie um programa que receberá uma expressão matemática qualquer que use parênteses armazenando-a em uma lista e analise se essa expressão está com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite a expressão: ')).strip()

if expressao.count('(') == expressao.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
