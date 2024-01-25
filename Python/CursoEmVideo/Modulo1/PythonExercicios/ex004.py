# Leia algo e imprima na tela o tipo lido e verifique as possibilidades que o valor pode assumir

dig = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(dig)} \nSó tem espaços? {dig.isspace()} \nÉ um número? {dig.isnumeric()} \nÉ alfabético? {dig.isalpha()} \nÉ alfanumérico? {dig.isalnum()} \nEstá em maiúsculas? {dig.isupper()} \nEstá em minúsculas? {dig.islower()} \nEstá em capitalizada? {dig.istitle()}')