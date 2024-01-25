'''
Crie um programa que tenha a função "leiaInt()" que funcionará de forma semelhante à função "input()" do python, porém fazendo a validação para aceitar apenas um valor inteiro.
'''
# Função Valida Inteiro
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
        else:
            print('\033[0;31mERRO! Digite um número inteiro.\033[m')


# Programa Principal
num = leiaInt('Digite um número inteiro: ')
print(f'\033[0;32mNúmero {num} é inteiro!\033[m')
