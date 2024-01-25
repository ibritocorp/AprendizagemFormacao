'''
Adapte o código do "ex108" criando uma função adicional chamada
"moeda()" que consiga mostra os valores como um valor monetário formatado.
'''
from ex108 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatmonet(valor)} é {moeda.formatmonet(moeda.metade(valor))}')
print(f'O dobro de {moeda.formatmonet(valor)} é {moeda.formatmonet(moeda.dobro(valor))}')
print(f'Aumentando 10%, temos {moeda.formatmonet(moeda.aumentar(valor))}')
print(f'Diminuindo 13%, temos {moeda.formatmonet(moeda.diminuir(valor))}')
