'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randrange

numComp = 0
cont = 0

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

while True:
    numComp = randrange(0, 11)
    numUser = int(input('Diga um valor: '))
    opcao = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    print('-' * 40)
    print(f'Você jogou {numUser} e o computador {numComp}. O total é {numUser + numComp}!')
    print('-' * 40)

    if opcao == 'P' and (numComp + numUser) % 2 == 0:
        print('PAR! Você VENCEU!')
        cont += 1
    elif opcao == 'I' and (numComp + numUser) % 2 != 0:
        print('ÍMPAR! Você VENCEU!')
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        break

    print('Vamos jogar novamente...')
    print('=-' * 20)

print(f'GAME OVER! {cont} vitória(s) conquistada(s)!')
