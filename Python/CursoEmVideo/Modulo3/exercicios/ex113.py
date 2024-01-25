'''
Reescreva a função "leiaInt()" do "ex104" incluindo a possibilidade da digitação de um tipo inválido. Aproveite e crie também uma função "leiaFloat()" com a mesma funcionalidade.
'''
import mod113

numeroInt = mod113.leiaInt('Digite um número inteiro: ')
numeroFloat = mod113.leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {numeroInt} e o real foi {numeroFloat}')
