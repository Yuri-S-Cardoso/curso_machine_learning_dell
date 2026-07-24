import pandas as pd
import matplotlib.pyplot as plt

frutas = pd.read_table('fruit_data_with_colors.txt',sep='\t')
freq = frutas['fruit_name'].value_counts()

# print para mostrar o nome de cada frutas e o número de vezes que cada uma aparece no dataset
print(freq, '\n')

#print para mostrar o gráfico de barras com a frequência de cada fruta
print(freq.plot(kind='bar'),plt.show(), '\n')

# print para mostrar o nome de cada fruta e o número de vezes que cada uma aparece no dataset, 
# mas agora com a função groupby
print(frutas['fruit_name'] == 'apple', '\n')

# variável macas recebe o resultado da comparação de cada elemento da coluna 'fruit_name' 
# com a string 'apple' e printa o resultado do dataset filtrado com a variável macas
macas = frutas['fruit_name'] == 'apple'
print(frutas[macas], '\n')

# print para mostrar onde a massa da fruta é maior que 175g, com o resultado do dataset filtrado
print(frutas['mass'] > 175, '\n')

# print para mostrar as maças cuja a massa é maior que 175g, com o resultado do dataset filtrado
print(frutas[macas & frutas['mass'] > 175], '\n')

# variável pesadas recebe o resultado da comparação de cada elemento da coluna 'mass'
# com o valor 175 e printa o resultado do dataset filtrado com a variável macas e pesadas 
pesadas = frutas['mass'] > 175
print(frutas[macas & pesadas], '\n')

# variaveis X1 e X2 recebem os valores das colunas 'width' (compriment) e 'height' (alturas) 
# do dataset filtrado com as variáveis macas e pesadas
X1 = frutas[macas & pesadas]['width']
X2 = frutas[macas & pesadas]['height']

# plt.scatter(X1, X2) cria um gráfico de dispersão com os valores das variáveis X1 e X2 e 
# plt.show() exibe o gráfico
plt.scatter(X1, X2)
plt.show()

# plt.scatter(X1, X2) cria um gráfico de dispersão com os valores das variáveis X1 e X2 e 
# plt.xlabel() e plt.ylabel() adicionam os rótulos aos eixos x e y, respectivamente e 
# plt.show() exibe o gráfico
plt.scatter(X1, X2)
plt.xlabel('Comprimento (cm)')
plt.ylabel('Altura (cm)')
plt.show()

# variaveis X1 e X2 recebem os valores das colunas 'width' (compriment) e 'height' (alturas), 
# plt.scatter(X1, X2) cria um gráfico de dispersão com os valores das variáveis X1 e X2, 
# plt.xlabel() e plt.ylabel() adicionam os rótulos aos eixos x e y, respectivamente, 
# plt.show() exibe o gráfico
X1 = frutas['width']
X2 = frutas['height']
plt.scatter(X1, X2)
plt.xlabel('Comprimento (cm)')
plt.ylabel('Altura (cm)')
plt.show()

# variável y recebe os valores da coluna 'fruit_label' do dataset frutas e printa o resultado
y = frutas['fruit_label']
print(y, '\n')

# plt.scatter(X1, X2, c=y) cria um gráfico de dispersão com os valores das variáveis X1, X2 e y     
# que garante que as cores serão de acordo com os rótulos das frutas
plt.scatter(X1, X2, c=y)
plt.xlabel('Comprimento (cm)')
plt.ylabel('Altura (cm)')
plt.show()


# Nesta aula deu para compreender como fazer leitura e análise de um conjunto de dados 
# com python.