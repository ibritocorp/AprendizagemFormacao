pessoa = list()
cadpessoas = list()

for c in range(0, 3):
    pessoa.append(str(input('Nome: ')).strip().capitalize())
    pessoa.append(int(input('Idade: ')))
    cadpessoas.append(pessoa[:])
    pessoa.clear()

for p in cadpessoas:
    print(p, end=' ')
    if p[1] >= 21:
        print('Maior')
        print()
    else:
        print('Menor')
        print()
