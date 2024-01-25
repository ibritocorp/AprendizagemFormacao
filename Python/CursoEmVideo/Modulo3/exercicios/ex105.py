'''
Faça um programa que tenha uma função chamada "notas()" que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

A) Quantidade de notas;
B) A maior nota;
C) A menor nota;
D) A média da turma;
E) A situação (opcional):
    > 7 = BOA
    > 4 > 6 = RAZOÁVEL
    < 4 = RUIM

Adicione também as docstrings da função.
'''
def notas(* nts, sit = False):
    """
    Calcula estatísticas básicas sobre notas fornecidas.
    
    Este função aceita uma lista variável de notas (*nts) e opcionalmente
    uma situação (sit) que indica a classificação da média das notas.

    Parâmetros:
    => nts (float): Uma lista de notas.
    => sit (bool): Se True, incluirá a situação com base na média das notas.

    Retorna:
    dict: Um dicionário contendo as estatísticas das notas.
        - 'total' (int): O número total de notas.
        - 'maior' (float): A maior nota.
        - 'menor' (float): A menor nota.
        - 'media' (float): A média das notas.
        - 'situacao' (str): A situação das notas, se sit=True.
            - 'RUIM': Se média <= 4;
            - 'RAZOÁVEL': Se 4 < média < 7;
            - 'BOA': Se média >= 7.
    """
    dic = {'total': len(nts),
           'maior': max(nts),
           'menor': min(nts),
           'media': sum(nts) / len(nts)
           }
    if sit:
        if dic['media'] <= 4:
            dic['situacao'] = 'RUIM'
        elif 4 < dic['media'] < 7:
            dic['situacao'] = 'RAZOÁVEL'
        else:
            dic['situacao'] = 'BOA'
    return dic


# Programa Principal
resp = notas(7, 7.5, 10, 9.9, sit = True)
print(resp)
help(notas)
