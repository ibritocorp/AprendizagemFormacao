'''
Crie um programa que leia nome, sexo e idade de várias pessoas guardando os dados em um dicionário e todos os dicionários em uma lista.
Mostre ao final:

A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.
'''

pessoa = {}
cadastros = []
mulheres = []
pessoasidadeacimamedia = []
somaidade = media = 0

print(f'{"=":=^60}\n{"CADASTRO DE PESSOAS":^60}\n{"=":=^60}')

while True:
    continua = ' '
    while continua not in 'NS':
        continua = str(input('Deseja preencher um novo cadastro [N - Não / S - Sim]? ')).strip().upper()[0]
    if continua == 'N':
        print(f'{"=":=^60}')
        break
    print(f'{"INSIRA OS DADOS SOLICITADOS":=^60}')
    pessoa['nome'] = str(input('Nome: ')).strip().title()

    definesexo = ' '
    while definesexo not in 'FM':
        definesexo = str(input('Sexo [F - Fem / M - Masc]: ')).strip().upper()[0]
    
    pessoa['sexo'] = definesexo
    pessoa['idade'] = int(input('Idade: '))
    cadastros.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
    print(f'{"=":=^60}')

    somaidade += pessoa['idade']

if len(cadastros) > 0:
    media = somaidade / len(cadastros)
    print(f'O grupo tem {len(cadastros)} pessoa(s).')
    print(f'A média de idade é de {media:.2f}.')
    if len(mulheres) > 0:
        print('Mulher(es) cadastrada(s):')
        for m in mulheres:
            print(f'{m["nome"]:^30}')

    for p in cadastros:
        if p['idade'] > media:
            pessoasidadeacimamedia.append(p.copy())

    if len(pessoasidadeacimamedia) > 0:
        print('Pessoa(s) com idade acima da média:')
        for p in pessoasidadeacimamedia:
            for k, v in p.items():
                print(f'{k}: {v}', end='; ')
            print()
else:
    print('Não há pessoa cadastrada!')

print(f'{"=":=^60}')
print(f'{"PROGRAMA ENCERRADO":^60}')
