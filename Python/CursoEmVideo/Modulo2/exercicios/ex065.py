'''
Crie um programa que leia vários números interos pelo teclado. No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuários se ele quer ou não continuar a digitar valores.
'''

cont = 0
soma = 0
maior = 0
menor = 0
opcao = ' '

while opcao != 'N':
    num = int(input('Digite um número inteiro: '))
    cont += 1
    soma += num
    if opcao == ' ':
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = input('Você deseja continuar? [S/N] ').strip().upper()[0]
    
media = soma / cont

print(f'A média é {media}, o menor número digitado foi {menor} e o maior {maior}.')
