def cabecalho(titulo):
    """
    Imprime um cabeçalho estilizado com um título.

    Esta função recebe um título como entrada e imprime um cabeçalho estilizado
    contendo o título centralizado.

    Parâmetros:
    titulo (str): O título que será exibido no cabeçalho.

    Retorna:
    None

    Exemplo:
    .: cabecalho("Bem-vindo ao Sistema")
    ---------------
    Bem-vindo ao Sistema
    ---------------
    """
    tam = len(titulo) + 4
    print(f'{"-":-^{tam}}')
    print(f'{titulo:^{tam}}')
    print(f'{"-":-^{tam}}')


def rodape(titulo):
    """
    Imprime um rodapé estilizado com um título.

    Esta função recebe um título como entrada e imprime um rodapé estilizado
    contendo o título centralizado, indicando o fim de uma seção.

    Parâmetros:
    titulo (str): O título que será exibido no rodapé.

    Retorna:
    None

    Exemplo:
    .: rodape("Fim do Relatório")
    ------------- FIM -------------
    """
    tam = len(titulo) + 4
    print(f'{" FIM ":-^{tam}}')
