pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(pessoas)
# print(pessoas[0]) - Essa estrutura não funciona, visto não haver índice ou chave "0".
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

pessoas['nome'] = 'Leandro'

for k, v in pessoas.items():
    print(f'{k.capitalize()} = {v}')

pessoas['peso'] = 98.5
print(pessoas)
