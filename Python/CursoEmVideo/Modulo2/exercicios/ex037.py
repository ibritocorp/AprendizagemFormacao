'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

1 - Para Binário
2 - Para Octal
3 - Para Hexadecimal
'''

num = int(input('Digite um número inteiro: '))
opcao = int(input('Digite o número correspondente ao tipo de conversão desejada conforme abaixo:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))

if opcao == 1:
    print('Binário')
elif opcao == 2:
    print('Octal')
elif opcao == 3:
    print('Hexadecimal')
else:
    print('Opção inválida!')
