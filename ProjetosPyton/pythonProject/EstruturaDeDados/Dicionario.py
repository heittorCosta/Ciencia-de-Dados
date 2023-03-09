#Cria um Dicionário
dados = {"Nomes": ["João", "José", "Maria"],
         "Idades": [25, 29, 15],
         "Notas": [50, 20, 86]
         }

#Imprime o Dicionário
print(dados)

#Acesso as notas e Idade de João
idade = dados["Idades"][0]
nota = dados["Notas"][0]

print("idade de João = ", idade)
print("Nota de João = ", nota )

#Inclusão de um novo Aluno Carlos de 25 anos e nota 90
dados["Nomes"].append("Carlos")
dados["Idades"].append(25)
dados["Notas"].append(90)
print(dados)