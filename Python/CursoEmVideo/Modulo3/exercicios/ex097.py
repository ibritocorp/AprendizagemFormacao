'''
Faça um programa que tenha uma função chamada "escreva()" que receberá um texto como parâmetro e mostrará uma mensagem com tamanho adaptável.

Exemplo:

escreva('Olá, Mundo!')

saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
'''
# Função p/ Reescrever o Texto
def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt:^{(len(txt) + 4)}}')
    print('~' * (len(txt) + 4))


# Programa Principal
escreva('Olá, Mundo!')
escreva('Curso de Python no YouTube')
