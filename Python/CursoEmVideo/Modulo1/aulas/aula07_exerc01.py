n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
# print(f'A soma vale {n1 + n2}')
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}\nO produto é {m}\nA divisão é {d:.2f}')
# Sintaxe ':.2f' da parte '{d:.2f}' formata o valor da variável para mostrar 2 casas flutuantes após o '.'
# Sintaxe ", end=' '" - print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}', end=' ') ao final do valor a ser impresso remove a quebra de linha do próximo print.

print(f'Divisão inteira {di}\nPotência {e}')
# Sintaxe '\n' no print quebra a linha
