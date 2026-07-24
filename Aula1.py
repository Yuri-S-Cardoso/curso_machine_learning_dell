import pandas as pd

frutas = pd.read_table('fruit_data_with_colors.txt',sep='\t')
print(frutas.head(5))
frutas.shape
print("A tabela tem", frutas.shape[0], "linhas e", frutas.shape[1], "colunas")

# Nesta aula aprendemos como efetuar a leitura de conjunto de dados e extrair infomações
# sobre a quantidade de linhas ou quantidade de elementos de um conjunto de dados e número 
# de colunas e função para apresentar as primeiras linhas do conjunto de dados.