'''
Crie um programa que tenha a função "leiaInt()" que funcionará de forma semelhante à função "input()" do python, porém fazendo a validação para aceitar apenas um valor inteiro.
'''
# Função Valida Inteiro
def leiaInt(msg):
    n = input(msg)
    while n.isnumeric() == False:
        print('\033[0;31mERRO! Digite um número inteiro.\033[m')
        n = input('Digite um número inteiro: ')
    return n


# Programa Principal
num = leiaInt('Digite um número inteiro: ')
print(f'\033[0;32mNúmero {num} é inteiro!\033[m')
