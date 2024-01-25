'''
Adicione uma função chamada "resumo()" ao módulo "moeda.py" criado nos desafios que mostre na tela algumas informações geradas pelas funções que já temos no módulo até aqui.
'''
from ex110 import moeda

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor, 50, 15)
