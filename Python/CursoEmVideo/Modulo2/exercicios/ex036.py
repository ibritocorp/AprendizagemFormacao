'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valCasa = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o valor do salário do comprador: R$'))
qtdParcelas = int(input('Digite a quantidade de parcelas: '))

valParcela = valCasa / qtdParcelas
percNecessário = salario * 0.3

if valParcela <= percNecessário:
    print('Financiamento Aprovado!')
else:
    print(f'Financiamento REPROVADO! Para pagar uma casa de R${valCasa:.2f} em {qtdParcelas} meses a prestação será de R${valParcela:.2f}! O valor da prestação ultrapassa o limite de R${percNecessário:.2f} (30% do salário). Para esse financiamento o salário deve ser igual ou maior que R${valParcela * 100 / 30:.2f}!')
