# Função teste()
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro (VARIÁVEL LOCAL) vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa Principal
a = 5
teste(a)
print(f'A fora (VARIÁVEL GLOBAL) vale {a}')
