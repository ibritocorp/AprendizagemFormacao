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


def leiaDinheiro(mensagem):
    """
    Lê um valor monetário inserido pelo usuário.

    Esta função recebe uma mensagem de prompt e permite que o usuário insira um valor
    monetário. Ela trata a entrada do usuário para garantir que o valor seja válido
    e o retorna como um número de ponto flutuante.

    Parâmetros:
    mensagem (str): A mensagem que será exibida para solicitar a entrada do usuário.

    Retorna:
    float: O valor monetário inserido pelo usuário.

    Exemplo:
    .: leiaDinheiro("Digite o valor: ")
    Digite o valor: R$ 1000,50
    1000.5
    """
    while True:
        valor = input(mensagem).replace(',', '.').strip()  # Substitui vírgula por ponto
        if valor.replace('.', '', 1).isdigit():
            return float(valor)
        else:
            print(f'\033[0;31mERRO! "{valor}" é um preço inválido.\033[m')
