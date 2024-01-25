"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

* O nome com todas as letras maiúsculas
* O nome com todas as letras minúsculas
* Quantas letras ao todo (sem considerar espeços)
* Quantas letras tem o primeiro nome
"""

# Meu código

"""
nome = input('Digite o nome completo: ')
print(f'Nome em caixa alta: {nome.upper()}')
print(f'Nome em caixa baixa: {nome.lower()}')
nomesemespaco = nome.replace(' ', '')
print(f'Quantidade de caracteres sem espaços: {len(nomesemespaco)}')
nomedividido = nome.split()
print(f'Quantidade de caracteres do primeiro nome: {len(nomedividido[0])}')
"""


# Código corrigido

nome = input('Digite o nome completo: ').strip()
print(f'Nome em caixa alta: {nome.upper()}')
print(f'Nome em caixa baixa: {nome.lower()}')
print(f'Quantidade de caracteres sem espaços: {len(nome) - nome.count(" ")}')
# print(f'Quantidade de caracteres do primeiro nome: {nome.find(" ")}')
# Ou utilizar a função 'split'
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])}')