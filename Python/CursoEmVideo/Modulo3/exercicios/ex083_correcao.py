expr = list(input('Digite a expressão: ').strip())
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
    