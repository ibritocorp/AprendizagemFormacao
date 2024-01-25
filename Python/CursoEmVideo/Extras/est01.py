while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite a operação desejada: ')

    numerosvalidos = None
    numero1float = 0
    numero2float = 0

    try:
        numero1float = float(numero1)
        numero2float = float(numero2)
        numerosvalidos = True

    except:
        numerosvalidos = None

    if numerosvalidos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if operador in '+-*/':
        numerosvalidos=True
        if operador == '+':
            print(numero1float+numero2float)
        elif operador == '-':
            print(numero1float-numero2float)
        elif operador == '*':
            print(numero1float*numero2float)
        elif operador == '/':
            print(numero1float/numero2float)
    else:
        numerosvalidos=False
        print("Operador inválido. Digite um operador correto.")
        continue

    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
