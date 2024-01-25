estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
estados = []

estados.append(estado1)
estados.append(estado2)

print(estados)
print(estados[0])
print(estados[1]['sigla'])

estado1['regiao'] = 'Sudeste'
estado2['regiao'] = 'Sudeste'

print(estados)
