filmes = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

print(filmes.values())
print(filmes.keys())
print(filmes.items())

for k, v in filmes.items():
    print(f'O {k} é {v}')