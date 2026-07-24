import pandas as pd

# na_values é um parâmetro que permite especificar valores faltantes no conjunto de dados. 
# Neste caso, estamos dizendo que o valor '.' e '?' deve ser tratado como um valor faltante (NaN).
data = pd.read_table('fruit_data_with_colors_miss.txt', na_values=['.', '?'])
#print(data, '\n') # printa o dataframe com os valores faltantes representados como NaN

# printa o dataframe com os valores faltantes preenchidos com 0
#print(data.fillna(0), '\n') 

# printa estatísticas descritivas do dataframe, como média, desvio padrão, valores mínimos e máximos, etc.   
#print(data.describe(), '\n') 

# printa o dataframe com os valores faltantes preenchidos com a média da coluna correspondente
#print(data.fillna(data.mean(numeric_only=True)))

# printa a contagem de cada valor único na coluna 'fruit_subtype'
#print(data['fruit_subtype'].value_counts()) 

# Preenche os valores faltantes com a média da coluna correspondente
data = data.fillna(data.mean(numeric_only=True)) 
#print(data, '\n') # printa o dataframe com os valores faltantes preenchidos com a média da coluna correspondente    

# Preenche os valores faltantes na coluna 'fruit_subtype' com o valor mais frequente (moda) da coluna
data['fruit_subtype'] = data['fruit_subtype'].fillna(data['fruit_subtype'].value_counts().idxmax()) 
print(data, '\n') # printa o dataframe com os valores faltantes preenchidos com a moda da coluna correspondente


# Nesta aula, aprendemos a lidar com valores faltantes em um conjunto de dados usando a 
# biblioteca pandas. Especificamente, vimos como identificar valores faltantes, preenchê-los 
# com zeros, médias ou modas, e como obter estatísticas descritivas do conjunto de dados. 
# Essas técnicas são essenciais para preparar os dados antes de aplicar algoritmos de 
# aprendizado de máquina.