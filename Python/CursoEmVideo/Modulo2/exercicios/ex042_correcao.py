r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: #Outra forma de comparar sem necessidade de "and", "or", etc...
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('As retas NÃO PODEM formar um triângulo!')
