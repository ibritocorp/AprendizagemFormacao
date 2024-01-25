# Função teste()
def teste(b):
    global a # Autoriza o uso da variável global e qualquer ação com a mesma, ela será alterada.
    a = 8 # O valor da variável a passará a ser 8 e até aqui o b já recebeu o valor 5.
    b += 4 # O valor de b será 5 + 4 que totaliza 9
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa Principal
a = 5
teste(a) # Após a chamada da função, a variável a sofreu a alteração do valor e já vale 8
print(f'A fora vale {a}') # Valor 8 é exibido
