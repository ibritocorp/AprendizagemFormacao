print('Olá, Mundo!')
# A comunidade utiliza aspas simples para textos/mensagens e todos textos/mensagens devem estar entre aspas
# Funções: Todas as funções possuem parênteses

print(7+4)
# Números não pedem aspas, são basicamente para cálculos

print('7'+'4')
# Números entre aspas com o '+' concatena
# Para a mesma ação a vírgula pode ser usada

#print('Olá' + 5)
# Erro ocorre, visto serem tipos diferentes com o operador
# As vezes a indicação é o '+', as vezes ','
print('Olá',5)
# Para correção, a indicação é o uso de vírgula de modo a concatenar

nome='Guanabara'
idade=25
peso=75.8
# Variáveis são objetos, objetos são um mais que variáveis
# Símbolo de '=' em variáveis considere 'Recebe'
print(nome, idade, peso)
print('Nome:', nome, 'Idade:', idade, 'Peso:', peso)

# Construção interativa
nome=input('Qual é o seu nome?')
idade=input('Qual é a sua idade?')
peso=input('Qual é o seu peso?')
print('Nome:', nome, 'Idade:', idade, 'Peso:', peso)