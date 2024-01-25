'''
Crie um programa que tenha um tupla com várias palavras (não usar acentos). Você deve mostrar para cada palavra, quais são suas vogais.
'''

palavras = ('fruta', 'luz', 'panela')

for palavra in palavras:
    print(f'A palavra "{palavra.upper()}" possui a(s) vogal(is): ', end='')
    
    for vogal in palavra:
        if vogal in 'aeiou':
            print(f'{vogal} ', end='')
    
    print('')
