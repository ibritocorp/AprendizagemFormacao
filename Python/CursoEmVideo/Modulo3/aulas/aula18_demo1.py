teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 22
print(teste)

galera.append(teste[:])
print(galera)
