################################# Primeiro Exemplo #################################
x = 1
while x<= 5:
    print(x)
    x = x + 1

################################# Segundo Exemplo #################################
fim = int(input("Digite o último número a imprimir"))
x = 1
while x <= fim:
    print(x)
    x = x + 1

################################# Terceiro Exemplo #################################
fim = int(input("Digite o último número a imprimir"))
x = 1
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

################################# Quarto Exemplo #################################
pontos = 0
questao = 1

while questao <=3:
    resposta = input("Resposta da questão %d" % questao)
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "d":
        pontos = pontos + 1
    questao += 1
print("O Aluno fez %d ponto(s)" % pontos)

################################# Quinto Exemplo #################################
n = 1
soma = 0

while n<=10:
    x = int(input("Digite o %d número" % n))
    soma = soma + x
    n = n + 1
print("Soma: %d" % soma)

################################# sexto Exemplo #################################
x = 1
soma = 0
while x<=5:
    n = int(input("%d Digite o número" % x))
    soma = soma + n
    x = x + 1
print("Média: %5.2f" % (soma/5))

################################# Sétimo Exemplo #################################
s = 0

while True:
    v = int(input("Digite um número a somar ou 0 para sair"))
    if v == 0:
        break
    s = s + v
print(s)

################################# Oitavo Exemplo #################################
valor = int(input("Digite o valor a ser pago:"))
cedulas = 0
atual = 50
aPagar = valor

while True:
    if atual <= aPagar:
        aPagar -= atual
        cedulas += 1
    else:
        print("%d Cédulas de R$%d" % (cedulas, atual))
        if aPagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

################################# Nono Exemplo #################################
tabuada = 1

while tabuada <= 10:
    numero = 1
    while numero <=10:
        print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
        numero += 1
    tabuada += 1