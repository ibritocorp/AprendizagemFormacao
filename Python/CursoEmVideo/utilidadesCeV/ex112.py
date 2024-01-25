'''
Dentro do pacote "utilidadesCeV" que criamos no "ex111" temos um módulo chamado "dado". Crie uma função chamada "leiaDinheiro()" que seja capaz de funcionar como a função "input()", mas com uma validação de dados para aceitar apenas valores que sejam monetários.
'''
from utilidadesCeV import moeda, dado

valor = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(valor, 35, 22)
