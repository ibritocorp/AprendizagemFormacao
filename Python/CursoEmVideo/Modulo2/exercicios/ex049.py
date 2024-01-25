'''
Refaça o exercício 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

n = int(input('Digite um número: ').strip())

for cont in range(1, 11):
    print(f'{cont} x {n} = {cont * n}')
    