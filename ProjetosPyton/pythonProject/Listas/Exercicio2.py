# Carregamento das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregamento dos dados a partir do .csv
dados = pd.read_csv("dados_pop.csv", header=1)  # header = informa a linha do cabeçalho
#print(dados)

# Processamento dos dados
dados_dict = dados.to_dict("list") # Convert o dataframe para um dicionario.
dados_sudeste = list(zip())
dados_nordeste = []
tamanho = len(dados_dict['Estado'])
contador = range(tamanho)
print(contador)
for i in contador:
    if (dados_dict['Estado'][i] in ("SP", "RJ", "MG", "ES")):
        dados_sudeste = dados_sudeste + [(dados_dict['Município'][i], dados_dict['População'][i])]

dados_sudeste.sort(key=[1])

for i in contador:
    if (dados_dict['Estado'][i] in ("MA", "PI", "CE", "RN", "PA", "PE", "AL", "SE", "PB")):
        dados_nordeste.append(dados_dict["Estado"][i])
print(dados_nordeste)


q1 = np.percentile(dados_dict['População'], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados_dict['População'], 75, method="averaged_inverted_cdf")
dq = q3 - q1

#Calcula od limites do boxplot
limit_inf = np.fmax(min(dados_dict["População"]), q1 - 1.5*dq)
limit_sup = np.fmin(max(dados_dict["População"]), q3 + 1.5*dq)

#Apresentação dos resultados
print(dados_sudeste)
print("Limite Inferior", limit_inf)
print("Limite Superior", limit_sup)

# diagrama_Brasil = plt.boxplot(dados_dict['População'], positions=[1], label=["Brasil"])
# diagrama_Sudeste = plt.boxplot(dados_sudeste, positions=[2], label=["Sudeste"])
# plt.show()