'''
Crie um programa que leia 5 valores numéricos, cadastre-os em uma lista já na possição correta de inserção (ascendente e sem usar o sort()) e ao final mostre a lista ordenada.
'''

valores = []

for i in range(0, 5):
    num = int(input('Digite um número inteiro qualquer: '))

    if len(valores) == 0 or num > valores[-1]:
        valores.append(num)
    else:
        cont = 0
        while cont < len(valores):
            if num <= valores[cont]:
                valores.insert(cont, num)
                break
            cont += 1

print(f'{"=":=^60}')
print(f'Os valores digitados em ordem crescente são: {valores}')
