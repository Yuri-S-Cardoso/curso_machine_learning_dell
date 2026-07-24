import pandas as pd

frutas = pd.read_table('fruit_data_with_colors.txt',sep='\t')
print(frutas.describe(),'\n')
# print para exibir apenas a análises estatísticas da coluna mass do conjunto de dados frutas
print(frutas.describe()['mass'], '\n')
# print para exibir apenas o valor mínimo da coluna mass do conjunto de dados frutas
print(frutas.describe()['mass']['min'], '\n')
# print para exibir apenas a coluna mass do conjunto de dados frutas
print(frutas['mass'], '\n')
# print para exibir apenas as colunas mass e color_score do conjunto de dados frutas
print(frutas[['mass','color_score']], '\n')
#print para exibir apenas as linhas 10 a 14 do conjunto de dados frutas
print(frutas[10:15], '\n')
# print para exibir apenas as linhas 10 a 14 do conjunto de dados frutas
i = 15
print(frutas[i-5:i], '\n')
#print para exibir apenas as linhas 15 a 19 do conjunto de dados frutas
print(frutas[i:i+5], '\n')
#print para exibir apenas as colunas mass e color_score das linhas 15 a 19 do conjunto de dados frutas
print(frutas[['mass','color_score']][i:i+5], '\n')

# Nesta aula aprendemos como efetuar análises estatísticas, como média, desvio padrão, 
# valor mínimo, valor máximo sob o conjunto de dados e selecionar apenas uma parte do 
# conjunto de dados, seja por colunas ou por linhas, ou ainda por colunas e linhas ao mesmo tempo.