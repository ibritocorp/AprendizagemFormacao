# Manipulando Cadeias de Texto (Caracteres)


# Cada caractere é alocado em um microespaço iniciando pelo índice 0
frase = 'Curso em Vídeo Python'

# Uso das aspas duplas três vezes serve para textos longos
print("""Welcome! Are you completely new to programming?
about why how to get started with Python. Fortunately
an experienced programmer in any programming language
(qhatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")


# Fatiamento

# Exibe o caractere contido no microespaço 9
print(frase[9])

# Exibe a cadeia de caracteres iniciando em 9 até a 13, visto que para em um anterior ao 14
print(frase[9:14])

# Exibe a cadeia de caracteres iniciando em 9 e pulando 2 índices a contar do caractere selecionado, ou seja, ele pega o caractere, pula uma casa e pega o próximo caractere
print(frase[9:21:2])

# Exibe a cadeia de caractere até o índice 4, visto que para em um anterior ao 5
print(frase[:5])

# Exibe a cadeia de caractere a partir do índice 15 até o final da cadeia
print(frase[15:])

# Exibe a cadeia de caractere a partir do índice 9 até o final da cadeia pulando 2 índices a contar do caractere de início
print(frase[9::3])


# Análise

# Exibe o tamanho (comprimento) da cadeia de texto
print(len(frase))

# Conta e exibe a quantidade de determinado caractere (no caso específico o 'o') numa cadeia de caracteres (case sensitive)
print(frase.count('o'))
# Conta e exibe a quantidade de determinado caractere (no caso específico o 'o') na cadeia de caracteres do índice 0 até o 12, anterior ao 13
print(frase.count('o', 0, 13))

# Localiza e exibe o primeiro índice que contenha o caractere ou cadeia de caracteres especificado
print(frase.find('deo'))
# O comando 'find' retorna o valor '-1' quando não localiza o caractere ou a cadeia de caracteres especificado
print(frase.find('android'))

# Verifica se um caractere ou uma cadeia de caracteres existe e exibe (print) 'True' para positivo ou 'False' para negativo
print('Curso' in frase)


# Transformação

# Uma lista de caracteres é imutável (não é possível alterá-la), mas é possível alterar através de métodos (bibliotecas)

# Substitui, se encontrado, o caractere ou a cadeia de caracteres especificado por outra especificada de forma secundária (no caso 'Python' por 'Android')
print(frase.replace('Python', 'Android'))

# Torna o caractere ou a cadeia de caracteres em caixa alta
print(frase.upper())

# Torna o caractere ou a cadeia de caracteres em caixa baixa
print(frase.lower())

# Torna o primeiro caractere em caixa alta caso ele não esteja e faz o mesmo com a cadeia de caracteres, porém colocando todos os demais caracteres em minúsculo
print(frase.capitalize())

# Identifica cada palavra (quando for uma cadeia de caracteres) e torna o primeiro caractere de cada palavra em maiúscula caso já não seja e o restante da palavra em minúscula
print(frase.title())


frase1 = '   Aprendendo Python  '

# Remove caracteres contendo espaço do início e final do caractere ou cadeia de caracteres
print(frase1.strip())

# Remove caracteres contendo espaço da direita de quem vê (final) do caractere ou cadeia de caracteres
print(frase1.rstrip())

# Remove caracteres contendo espaço da direita de quem vê (final) do caractere ou cadeia de caracteres
print(frase1.lstrip())


# Divisão

# Divide caracteres ou uma cadeia de caracteres em outras listas (identifica pela separação por espaços para cadeias de caracteres) e redefine os índices iniciando por 0 em cada palavra dividida
print(frase.split())

# Juntar uma lista de cadeia de caracteres separando pelo caractere especificado
print('-'.join(frase))
