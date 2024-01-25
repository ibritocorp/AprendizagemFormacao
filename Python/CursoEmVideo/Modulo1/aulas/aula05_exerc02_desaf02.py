n = input('Digite algo: ')
print(f'O tipo inserido é: {type(n)} \nÉ um número? {n.isnumeric()} \nÉ uma string? {n.isalpha()} \nÉ um número? {n.isalnum()}')