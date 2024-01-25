def metade(val=0, monet=True):
    """
    Retorna a metade de um valor numérico.

    Esta função recebe um valor numérico e retorna a sua metade.

    Parâmetros:
    val (float or int): O valor numérico do qual se deseja obter a metade.

    Retorna:
    float: A metade do valor fornecido.

    Exemplos:
    .: metade(10)
    5.0
    .: metade(7.5)
    3.75
    """
    val /= 2
    if monet:
        return formatmonet(val)
    else:
        return val


def dobro(val, monet=True):
    """
    Retorna o dobro de um valor numérico.

    Esta função recebe um valor numérico e retorna o seu dobro.

    Parâmetros:
    val (float or int): O valor numérico do qual se deseja obter o dobro.

    Retorna:
    float: O dobro do valor fornecido.

    Exemplos:
    .: dobro(5)
    10
    .: dobro(2.5)
    5.0
    """
    val *= 2
    if monet:
        return formatmonet(val)
    else:
        return val


def aumentar(val, percent=10, monet=True):
    """
    Retorna um valor aumentado por uma porcentagem.

    Esta função recebe um valor numérico e opcionalmente uma porcentagem de aumento.
    Ela retorna o valor aumentado de acordo com a porcentagem fornecida.

    Parâmetros:
    val (float or int): O valor numérico que será aumentado.
    percent (float, optional): A porcentagem de aumento. O valor padrão é 10.

    Retorna:
    float: O valor aumentado de acordo com a porcentagem fornecida.

    Exemplos:
    .: aumentar(100, 20)
    120.0
    .: aumentar(50)
    55.0
    """
    val += val * (percent / 100)
    if monet:
        return formatmonet(val)
    else:
        return val


def diminuir(val, percent=13, monet=True):
    """
    Retorna um valor diminuído por uma porcentagem.

    Esta função recebe um valor numérico e opcionalmente uma porcentagem de diminuição.
    Ela retorna o valor diminuído de acordo com a porcentagem fornecida.

    Parâmetros:
    val (float or int): O valor numérico que será diminuído.
    percent (float, optional): A porcentagem de diminuição. O valor padrão é 13.

    Retorna:
    float: O valor diminuído de acordo com a porcentagem fornecida.

    Exemplos:
    .: diminuir(100, 20)
    80.0
    .: diminuir(50)
    43.5
    """
    val -= val * (percent / 100)
    if monet:
        return formatmonet(val)
    else:
        return val


def formatmonet(val, simb='R$'):
    return f'{simb}{val:.2f}'.replace('.', ',')
