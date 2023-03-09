#Carregando as bibliotecas
import matplotlib.pyplot as plt
import numpy

#Carregando os dados
dados = {"Ramo": ["Automóvel", "Saúde", "Incêndio", "Vida", "Riscos Diversos", "Habitação", "Transporte", "Acidentes Pessoais", "Obrigatório Veículos", "Riscos de Engenharia", "Responsabilidade Civil"],
         "%": [33.6, 14.0, 12.9, 12.2, 5.5, 5.3, 3.1, 2.9, 1.7, 1.0, 0.9]
         }
valores = dados["%"]
boxplot = plt.boxplot(valores)
plt.show()