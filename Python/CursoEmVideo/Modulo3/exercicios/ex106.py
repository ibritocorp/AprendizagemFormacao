'''
Faça um minisistema que utilize o Interactive Help do Python, ou seja, o usuário vai digitar o comando e o manual vai aparecer. Quando o usuários digitar 'FIM', o programa se encerrará.

Obs.: Utilize cores.
'''
cor = ('\033[m',            # 0 - Sem cores
       '\033[0;30;41m',     # 1 - Vermelho
       '\033[0;30;42m',     # 2 - Verde
       '\033[0;30;43m',     # 3 - Amarelo
       '\033[0;30;44m',     # 4 - Azul
       '\033[0;30;45m',     # 5 - Roxo
       '\033[7;30m'         # 6 - Branco
       )

def cabecalho(titulo, c):
    tam = len(titulo) + 4
    print(cor[c], end='')
    print(f'{"~":~^{tam}}')
    print(f'{titulo:^{tam}}')
    print(f'{"~":~^{tam}}')
    print(cor[0], end='')


def ajuda(comando):
    cabecalho(f'Manual do comando \'{comando}\'', 4)
    print(cor[6], end='')
    help(comando)
    print(cor[0], end='')


# Programa Principal
while True:
    cabecalho('SISTEMA DE AJUDA PyHELP', 3)
    termo = str(input('Digite a Função ou Biblioteca para visualizar o Manual ou "FIM" para encerrar: ')).strip()
    if termo.upper() == 'FIM':
        cabecalho('ATÉ LOGO!', 1)
        break
    else:
        ajuda(termo)
