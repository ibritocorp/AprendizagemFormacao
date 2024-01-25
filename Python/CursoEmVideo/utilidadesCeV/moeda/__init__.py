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
    return formatmonet(val) if monet else val


def dobro(val=0, monet=True):
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
    return formatmonet(val) if monet else val


def aumentar(val=0, percent=10, monet=True):
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
    return formatmonet(val) if monet else val


def diminuir(val=0, percent=13, monet=True):
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
    return formatmonet(val) if monet else val


def formatmonet(val=0, simb='R$'):
    """
    Formata um valor numérico como uma string monetária.

    Esta função recebe um valor numérico e opcionalmente um símbolo de moeda.
    Ela retorna uma string formatada que representa o valor como uma quantia monetária.

    Parâmetros:
    val (float or int): O valor numérico que será formatado.
    simb (str, optional): O símbolo de moeda a ser usado. O valor padrão é 'R$'.

    Retorna:
    str: Uma string formatada representando o valor como uma quantia monetária.

    Exemplos:
    .: formatmonet(1000.5, 'US$')
    'US$1.000,50'
    .: formatmonet(50.75)
    'R$50,75'
    """
    return f'{simb}{val:.2f}'.replace('.', ',')


def resumo(val=0, percentaum=0, percentred=0, monet=True):
    """
    Imprime um resumo analítico de um valor monetário.

    Esta função recebe um valor monetário, opcionalmente porcentagens de aumento
    e redução, e um indicador de formatação monetária. Ela imprime um resumo
    analítico que inclui o preço analisado, o dobro do preço, a metade do preço,
    o aumento percentual e a redução percentual.

    Parâmetros:
    val (float or int, optional): O valor monetário a ser analisado. O valor padrão é 0.
    percentaum (float, optional): A porcentagem de aumento. O valor padrão é 0.
    percentred (float, optional): A porcentagem de redução. O valor padrão é 0.
    monet (bool, optional): Indica se o valor deve ser formatado como uma quantia monetária. O valor padrão é True.

    Retorna:
    None

    Exemplo:
    >>> resumo(1000, 20, 10)
    ---------- RESUMO DO VALOR -----------
    Preço analisado:          R$1.000,00
    Dobro do preço:           R$2.000,00
    Metade do preço:          R$500,00
    20% de aumento:           R$1.200,00
    10% de redução:           R$900,00
    ----------------- FIM ----------------
    """
    from utilidadesCeV import dado
    dado.cabecalho('-------- RESUMO DO VALOR --------')
    if monet:
        print(f'Preço analisado: {formatmonet(val, "R$"):>20}')
    else:
        print(f'Preço analisado:{val:>21}')
    print(f'Dobro do preço: {dobro(val, monet):>21}')
    print(f'Metade do preço: {metade(val, monet):>20}')
    print(f'{percentaum}% de aumento: {aumentar(val, percentaum, monet):>21}')
    print(f'{percentred}% de redução: {diminuir(val, percentred, monet):>21}')
    dado.rodape('-------- RESUMO DO VALOR --------')
