'''
Modifique as funções que foram criadas no "ex107" para que elas aceitem um parâmetro a mais que informará se o valor retornado por elas será ou não formatado pela função "moeda()" desenvolvido no "ex108".
'''
from ex109 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatmonet(valor)} é {moeda.metade(valor)}')
print(f'O dobro de {moeda.formatmonet(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(valor)}')
