'''
Faça um programa que leia nome e peso de várias pessoas guardando esses valores numa lista e no final mostre:

A) Quantas pessoas foram cadastradas;
B) Pessoa(s) mais pesada(s);
C) Pessoa(s) mais leve(s).
'''

pessoas = []
listmenor = []
listmaior = []
menor_peso = maior_peso = 0

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    peso = float(input('Peso: '))

    if len(pessoas) == 0:
        menor_peso = maior_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        if peso > maior_peso:
            maior_peso = peso

    pessoas.append([nome, peso])

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

for p in pessoas:
    if p[1] == menor_peso:
        listmenor.append(p[0])
    
    if p[1] == maior_peso:
        listmaior.append(p[0])

print(f'{"=":=^60}')
print(f'Existe(m) {len(pessoas)} cadastro(s).')
print(f'O menor peso foi {menor_peso}kg. Peso de {listmenor}')
print(f'O maior peso foi {maior_peso}kg. Peso de {listmaior}')
