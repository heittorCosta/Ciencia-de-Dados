# Escreva um programa em Python que calcule o salário líquido de um Professor.
# Para elaborar o programa, é necessário possuir alguns dados, tais como:
# Valor da hora-aula: R$ 25,00
# Número de horas trabalhadas no mês: 120
# Percentual de desconto do INSS: 8%

valorHora = 25
horasMes = 120

salario = valorHora * horasMes
descINSS = salario * 0.08
salarioLiq = salario - descINSS
print("O salário líquido é %10.2f " % salarioLiq)
