'''
Crie um pograma que tenha uma função chamada "voto()" para receber como parâmetro o ano de nascimento de uma pessoa. Essa função retornará um valor literal indicando se a pessoa tem voto "NEGADO", "OPCIONAL" ou "OBRIGATÓRIO" nas eleições.
'''
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Idade: {idade}, voto NEGADO!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Idade: {idade}, voto FACULTATIVO!'
    else:
        return f'Idade: {idade}, voto OBRIGATÓRIO!'


# Programa Principal
nasc = int(input('Digite o ano de nascimento: '))
result = voto(nasc)
print(result)
