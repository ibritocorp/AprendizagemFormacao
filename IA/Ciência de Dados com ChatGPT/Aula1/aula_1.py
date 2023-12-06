import pandas as pd

# Carregar os dados do Excel
caminho_arquivo = r'C:\Users\itilo\Downloads\Ciência de Dados com ChatGPT\CONJUNTO DE DADOS PARA EXPERIÊNCIAS\titanic-preprocessado.xlsx'
dados_titanic = pd.read_excel(caminho_arquivo)

# Exibir as primeiras linhas dos dados para verificar se foram carregados corretamente
print(dados_titanic.head())

# Estatísticas descritivas dos dados
print("\nEstatísticas Descritivas:")
print(dados_titanic.describe())

# Contagem de sobreviventes
sobreviventes = dados_titanic['Survived'].sum()
print("\nNúmero de Sobreviventes:", sobreviventes)

# Média de idade dos passageiros
media_idade = dados_titanic['Age'].mean()
print("\nMédia de Idade:", media_idade)

# Contagem de passageiros por classe
contagem_classe = dados_titanic['Pclass'].value_counts()
print("\nContagem de Passageiros por Classe:")
print(contagem_classe)

# Gráfico de contagem de sobreviventes por gênero
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x='Survived', hue='Sex', data=dados_titanic)
plt.title('Contagem de Sobreviventes por Gênero')
plt.show()
