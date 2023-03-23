# Carregamento das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregamento dos dados a partir do .csv
dados = pd.read_csv("dados_seguros.csv", header=1)  # header = informa a linha do cabeçalho

# Processamento dos dados
dados_dict = dados.to_dict("list") # Convert o dataframe para um dicionario.
q1 = np.percentile(dados_dict['Fatia de Mercado'], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados_dict['Fatia de Mercado'], 75, method="averaged_inverted_cdf")

dq = q3 - q1

#Calcula od limites do boxplot
limit_inf = np.fmax(min(dados_dict["Fatia de Mercado"]), q1 - 1.5*dq)
limit_sup = np.fmin(max(dados_dict["Fatia de Mercado"]), q3 + 1.5*dq)

#Determina o tamanho dos dados
tamanho = len(dados_dict['Fatia de Mercado'])
contador = range(tamanho)
#identifica um Outliers
for i in contador:
    if (dados_dict['Fatia de Mercado'][i] > limit_sup) or (dados_dict['Fatia de Mercado'][i] < limit_inf):
        print("Outlier: ", dados_dict["Ramo"][i], " - ", dados_dict['Fatia de Mercado'][i])

#Apresentação dos resultados
print(dados_dict)
print("Limite Inferior", limit_inf)
print("Limite Superior", limit_sup)

diagrama = plt.boxplot(dados_dict['Fatia de Mercado'])
plt.show()