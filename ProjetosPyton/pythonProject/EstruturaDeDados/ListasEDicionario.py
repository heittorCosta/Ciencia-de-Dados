#Dados Originais
lista_dados = [-0.5, 1.8, 43.8, 52, 2.6, 7.8, 9.8, -2.5]

#Imprime a lista original
print(lista_dados)

#Imprime o tamanho da lista
x = len(lista_dados)
print("Tamanho da lista", x)

#Imprime a lista ordenada
lista_dados.sort()
print(lista_dados)

#Imprime o menor elemento
print("Menor elemento", lista_dados[0])

#Imprime maior do que 0
for i in range(len(lista_dados)):
    if lista_dados[i] > 0:
        print(lista_dados[i])

#Adiciona um novo valor na lista
lista_dados.append(4.5)
print(lista_dados)
lista_dados.sort()
print(lista_dados)

