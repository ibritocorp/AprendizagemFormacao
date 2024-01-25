def leiaInt(msg):
    """
    Lê um número inteiro inserido pelo usuário.

    Esta função recebe uma mensagem de prompt e permite que o usuário insira um número
    inteiro. Ela trata a entrada do usuário para garantir que o valor seja um número
    inteiro válido.

    Parâmetros:
    msg (str): A mensagem que será exibida para solicitar a entrada do usuário.

    Retorna:
    int: O número inteiro inserido pelo usuário.

    Exemplo:
    => leiaInt("Digite um número inteiro: ")
    Digite um número inteiro: 42
    42
    """
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
        else:
            return num


def leiaFloat(msg):
    """
    Lê um número real inserido pelo usuário.

    Esta função recebe uma mensagem de prompt e permite que o usuário insira um número
    real. Ela trata a entrada do usuário para garantir que o valor seja um número
    real válido.

    Parâmetros:
    msg (str): A mensagem que será exibida para solicitar a entrada do usuário.

    Retorna:
    float: O número real inserido pelo usuário.

    Exemplo:
    => leiaFloat("Digite um número real: ")
    Digite um número real: 3.14
    3.14
    """
    while True:
        try:
            num = float(f'{input(msg)}')
        except KeyboardInterrupt:
            print('\033[0;31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número real válido.\033[m')
        else:
            return num
