def parOuImpar(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


if parOuImpar(10):
    print('Número PAR')
else:
    print('Número ÍMPAR')
