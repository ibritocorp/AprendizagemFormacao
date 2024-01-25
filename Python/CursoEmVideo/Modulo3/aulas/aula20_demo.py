def criar_cabecalho(titulo):
    tamanho_linha = 40
    linha = '-' * tamanho_linha
    espacos = (tamanho_linha - len(titulo)) // 2

    cabecalho = f"{linha}\n{' ' * espacos}{titulo}\n{linha}"
    print(cabecalho)
    return cabecalho

#titulo = 'teste'#input("Digite o título para o cabeçalho: ")
criar_cabecalho('TÍTULO')
print()
criar_cabecalho('TESTE TESTANDO')
#cabecalho_formatado = criar_cabecalho(titulo)
#print(cabecalho_formatado)

def mostraLinha():
    print(f'{"-":-^50}')


mostraLinha()
print(f'{"SISTEMA DE ALUNOS":^50}')
mostraLinha()


def mostraCabecalho(titulo):
    print(f'{"-":-^50}')
    print(f'{titulo:^50}')
    print(f'{"-":-^50}')


mostraCabecalho('TESTE')
