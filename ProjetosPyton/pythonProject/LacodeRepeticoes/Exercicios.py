# Solicita ao usuário os dois números a serem multiplicados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Inicializa as variáveis
resultado = 0
contador = 0

# Realiza a multiplicação usando somas sucessivas
while contador < num2:
    resultado += num1
    contador += 1

# Exibe o resultado na tela
print(f"O resultado da multiplicação é: {resultado}")



0 + 2
6