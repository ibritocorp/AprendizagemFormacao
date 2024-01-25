def cabecalho(titulo, acresc=20):
    """
    Imprime um cabeçalho estilizado com um título.

    Esta função recebe um título como entrada e, opcionalmente, um valor para o acréscimo
    no tamanho do cabeçalho. Ela imprime um cabeçalho estilizado contendo o título centralizado.

    Parâmetros:
    titulo (str): O título que será exibido no cabeçalho.
    acresc (int, optional): O acréscimo no tamanho do cabeçalho. O valor padrão é 20.

    Retorna:
    None

    Exemplo:
    => cabecalho("Bem-vindo ao Sistema", 30)
    ------------------------------
         Bem-vindo ao Sistema
    ------------------------------
    """
    tam = len(titulo) + acresc
    print(f'{"-":-^{tam}}')
    print(f'{titulo:^{tam}}')
    print(f'{"-":-^{tam}}')



def rodape(titulo, acresc=20):
    """
    Imprime um rodapé estilizado com um título.

    Esta função recebe um título como entrada e, opcionalmente, um valor para o acréscimo
    no tamanho do rodapé. Ela imprime um rodapé estilizado contendo o título centralizado,
    indicando o fim de uma seção.

    Parâmetros:
    titulo (str): O título que será exibido no rodapé.
    acresc (int, optional): O acréscimo no tamanho do rodapé. O valor padrão é 20.

    Retorna:
    None

    Exemplo:
    => rodape("Sistema encerrado", 25)
    ------------------------------
          Sistema encerrado
    ------------------------------
    """
    tam = len(titulo) + acresc
    print(f'{"-":-^{tam}}')
    print(f'{titulo:^{tam}}')
    print(f'{"-":-^{tam}}')


def criaLinha(titulo, acresc=20):
    """
    Cria uma linha estilizada.

    Esta função recebe um título como entrada e, opcionalmente, um valor para o acréscimo
    no tamanho da linha. Ela imprime uma linha estilizada contendo o caractere '-'.

    Parâmetros:
    titulo (str): O título é usado apenas para calcular o tamanho da linha.
    acresc (int, optional): O acréscimo no tamanho da linha. O valor padrão é 20.

    Retorna:
    None

    Exemplo:
    => criaLinha("Título da Seção", 15)
    -------------------------------
    """
    tam = len(titulo) + acresc
    print(f'{"-":-^{tam}}')
    