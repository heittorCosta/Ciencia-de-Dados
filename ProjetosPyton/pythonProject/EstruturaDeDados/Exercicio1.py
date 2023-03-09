#Carregando as Bibliotecas
import matplotlib.pyplot as plt
import numpy as np

#Entrando com os dados
dados = [45,56,-89,23.4,1.5,2.5,5.5,10,-50,1]
dados.append(-12.5)
dados2 = dados

#Processamento dos dados
Q1 = np.percentile(dados2, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(dados2, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(dados2, 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1

Limite_inferior = np.fmax(min(dados2), Q1-1.5*DQ)
Limite_superior = np.fmin(max(dados2), Q3+1.5*DQ)

dados3 = []

for i in range(len(dados2)):
    if dados2[i] < Limite_superior and dados2[i] > Limite_inferior:
        dados3.append(dados2[i])

boxplot1 = plt.boxplot(dados2, positions=[1])
boxplot2 = plt.boxplot(dados3, positions=[2])
plt.show()