def fatorial(num = 1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

n = int(input('Digite um número inteiro: '))
f1 = fatorial(n)
f2 = fatorial(f1)
print(f'O fatorial de {n} é {f1} e o fatorial de {f1} é {f2}.')
