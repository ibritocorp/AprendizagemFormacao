'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:

- Média abaixo de 5: REPROVADO
- Média entre 5 e 6.9: RECUPERAÇÃO
- Média igual ou acima de 7: APROVADO
'''

n1 = float(input('Digite a primeira nota: ').strip())
n2 = float(input('Digite a segunda nota: ').strip())

media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
    