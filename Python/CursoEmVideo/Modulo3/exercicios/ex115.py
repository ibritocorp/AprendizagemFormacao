'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo se nome e idade em um arquivo de texto simples. O sistema só vai ter duas opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
'''
import mod115

arq = 'cadEx115.txt'

if mod115.arqExiste(arq):
    print('Arquivo existe')
else:
    mod115.criarArquivo(arq)
    