pessoa = ['Ítalo', 35]

galera = list()

galera.append(pessoa[:])

pessoa = ['Gabriel', 40]

galera.append(pessoa[:])

print(galera)

for p in galera:
    print(p)

for p in galera:
    print(f'A idade de {p[0]} é {p[1]}.')
