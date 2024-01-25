'''
Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa mostre:

* A média de idade do grupo;
* O nome do homem mais velho;
* Quantas mulheres têm menos de 21 anos.
'''

somaIdade = 0
idadeHomem = 0
nomeHomem = ''
contMulherMenor = 0

for i in range(0, 4):
    print('-' * 30)
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: ').strip())
    sexo = input('Digite o sexo (M - Masculino | F - Feminino ): ').strip()
    
    somaIdade += idade

    if sexo == 'M':
        if idade > idadeHomem:
            idadeHomem = idade
            nomeHomem = nome
    else:
        if idade < 21:
            contMulherMenor += 1

print(f'Média de idade do grupo: {somaIdade / 4}\nNome do homem mais velho: {nomeHomem}\n{contMulherMenor} mulher(es) possui(em) menos de 21 anos')
