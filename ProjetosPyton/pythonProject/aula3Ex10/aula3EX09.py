#EX09 - Em uma eleição sindical concorreram ao cargo de presidente três
# candidatos (representados pelas variáveis A, B e C). Durante a apuração
# dos votos foram computados votos nulos e em branco, além dos votos válidos
# para cada candidato. Deve ser criado um programa de computador que faça a
# leitura da quantidade de votos válidos para cada candidato, além de também ler a
# quantidade de votos nulos e em branco. Ao final o programa deve apresentar o número
# total de eleitores, considerando votos válidos, nulos e em branco; o percentual correspondente
# de votos válidos em relação à quantidade de eleitores; o percentual correspondente
# de votos válidos do candidato A em relação à quantidade de eleitores; o percentual
# correspondente de votos válidos do candidato B em relação à quantidade de eleitores;
# o percentual correspondente de votos válidos do candidato C em relação à quantidade de eleitores;
# o percentual correspondente de votos nulos em relação à quantidade de eleitores; e por último o percentual
# correspondente de votos em branco em relação à quantidade de eleitores.


votos_A = 5000
votos_B = 4000
votos_C = 3000
nulos = 500
brancos = 400

res = votos_A + votos_B + votos_C + nulos + brancos
print("A quantidade de eleitores é: ", res)
print("A quantidade de votos válidos para o candidato A é:", votos_A)
print("A quantidade de votos válidos para o candidato B é:", votos_B)
print("A quantidade de votos válidos para o candidato C é:", votos_C)
print("A quantidade de votos nulos é:", nulos)
print("A quantidade de votos em branco é:", brancos)
