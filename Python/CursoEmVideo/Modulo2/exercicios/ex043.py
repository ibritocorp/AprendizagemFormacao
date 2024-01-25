'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade mórbida
'''

peso = float(input('Digite o peso: (kg) '))
altura = float(input('Digite a altura: (m) '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 25:
    print('Peso ideal!')
elif imc < 30:
    print('Sobrepeso!')
elif imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')
