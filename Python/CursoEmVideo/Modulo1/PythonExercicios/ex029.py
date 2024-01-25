"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite.
"""

# Importação de função 'sleep' da biblioteca 'time' para incrementar o código
from time import sleep

# Montagem de cabeçalho para incrementar estética
print('-=-' * 20)
print('<<<<<<<<<<<<<<< SISTEMA DE EMISSÃO DE MULTAS >>>>>>>>>>>>>>>')
print('-=-' * 20)

# Definição do limite de velocidade
maximo = 80.00

# Estrutura de leitura da velocidade via teclado
velocidade = float(input('Qual é a velocidade atual do carro? Especifique em km/h: ').strip())

# Estrutura condicional
if velocidade > maximo:
    multa = (velocidade - maximo) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de {maximo:.0f} km/h!')

    # Montagem do extrato da multa
    sleep(2)
    print('-' * 60)
    print(f'Limite de velocidade: {maximo:.0f} km/h')
    print(f'Velocidade excedida: {velocidade - maximo:.2f} km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')
    print('-' * 60)

# Mensagem padrão a todas as consultas
print('Tenha um bom dia! Dirija com segurança!')