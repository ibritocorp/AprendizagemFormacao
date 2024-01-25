'''
Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:

- À vista (dinheiro/cheque): 10% de desconto
- À vista (cartão): 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''

print(f'{" LOJAS GUANABARA ":=^40}')

valCompra = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista (dinheiro/cheque)
[2] à vista (cartão)
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = valCompra - (valCompra * 0.1)
elif opcao == 2:
    total = valCompra - (valCompra * 0.05)
elif opcao == 3:
    total = valCompra
    print(f'Sua compra será parcelada em 2x de R${valCompra / 2:.2f}.')
elif opcao == 4:
    qtdParcelas = int(input('Quantas parcelas? '))
    total = valCompra * 1.2
    print(f'Sua compra será parcelada em {qtdParcelas}x de {total / qtdParcelas:.2f} COM JUROS.')
else:
    total = valCompra
    print('Opção inválida. Tente novamente.')

print(f'Sua compra de R${valCompra:.2f} vai custar R${total:.2f} no final.')
