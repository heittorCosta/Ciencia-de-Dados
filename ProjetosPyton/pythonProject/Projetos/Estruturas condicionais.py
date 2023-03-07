'''
Aula 04 - Estruturas Condicionais
Um bloco é um conjunto de comandos agrupados. Os programas Python são estruturados através de indentação,
ou seja, os blocos são definidos pelo seu espaçamento (tabs) em relação ao início da linha.
Geralmente um tab ou 4 espaços, depende da IDE
'''

'''
# Exemplo 1 comando if simples
n1 = float(input("Digite a primeira nota do bimestre: "))
n2 = float(input("Digite a segunda nota do bimestre: "))
media = (n1+n2)/2
if media>=7:
    print("Você passou!")
if media<7 :
    print("Você não passou!")
print("################################################################################")
'''

'''
# Exemplo 2 comando if com a adição do else
n1 = float(input("Digite a primeira nota do bimestre: "))
n2 = float(input("Digite a segunda nota do bimestre: "))
media = (n1+n2)/2
if media>=7:
    print("Você passou!")
else:
    print("Você não passou!")
print("##################################################################################")
'''

'''
#Exemplo 3 comando if com a adiçao do elif
n1 = float(input("Digite a primeira nota do bimestre: ")) #entrada de dados
n2 = float(input("Digite a segunda nota do bimestre: "))#entrada de dados
media = (n1+n2)/2 #processamanto
if media>=7:
    print("Você passou!")
elif (media >= 5 and media <= 7): ### operadores relacionais e lógicos (range de 5 a 7 são verdadeiros)
    print("Você não passou, recuperação na próxima semana!")
elif (media < 5):
    print("Você infelizmente está eliminado!")
print("##################################################################################")
'''
'''
#Exemplo 4 blocos aninhados (usar 4 espaços para cada bloco de aninhamento)
n1 = float(input("Digite a primeira nota do bimestre: "))
n2 = float(input("Digite a segunda nota do bimestre: "))
media = (n1+n2)/2
if media >=7:
    print("Você atingiu a média mínima. Nota = %2.1f!" % (media),end="")
    if media > 8:
        print("E também a maioria dos criterios desejáveis!", end="") # end escreve e fica na mesma linha
        if media > 9 :
            print("Com esses a mais você é nosso alunis ouro!!!")
print("\n##############################################################################################")
'''

#Exemplo 5 blocos aninhados e tentativa de corrigir entradas equivocadas do usuário
num=palavra=input("Digite um numero inteiro de 1 a 3: ") # ler sem conversão
palavra=palavra.replace(".","")                          # o método replace da classe str troca um
                                                         # caracter por outro ou nenhum como
                                                         # seria nesse nosso caso
palavra=palavra.replace("-","")
if(palavra.isdecimal()):                                 #outro método da classe str que testa se o caracter é ou não algo entre 0 a 9
    num=float(num)
    if  num==1:
            print("um")
    else:
        if(num==2):
            print("dois")
        else:
            if(num==3):
                print("três")
            else:
                if(num>4 and num<5):
                    print("Intervalo de numeros maiores que 4 e menores que 5")
                else:
                    print("Número fora do intervalo")
else:
    print("Não pode ser número o que foi digitado!!!")
print("##################################################################################################")



'''
Exercícios 
1) Escreva um programa em python que leia dois números decimais, leia a operação desejada 
dentre adição, subtração, multiplicação ou divisão e mostre o seu resultado com duas casas 
decimais. Não permita a possibilidade do sistema tentar calcular uma divisão por zero ou a
leitura de caracteres que não possam ser números.

2)Escreva um programa em python para calcular os valores de imc a partir de entradas de 
dados especificos como peso e altura da pessoa. Não permita a entrada de valores que não 
possam ser numeros. O sistema deve trazer o resultado escrito do IMC e não o cálculo.
Não permita que o usuário entre com valores que não possam ser números
IMC = Peso[kg] ÷ (Altura²[m]) 
baixo peso < 18,5
18,5 >= peso normal < 25
25 >= pre obesidade < 30
30 >= obesidade grau 1 < 35
35 >= obesidade grau 2 < 40 
obesidade mórbida >= 40 

3) Calcule um polinômio do segundo grau através da fómula de báskara ax²+ bx + c. Não 
permita o sistema tentar calcular divisão por zero, raiz negativa ou entrada de valores 
que não sejam números. Mostrar quantas raizes o sistema deve gerar: nenhuma(se for numero
complexo com raiz negativa, uma ou duas) e seus valores sempre com duas casas decimais.

4) O software deve permitir a leitura de um código cifrado (protocolo) que contenha 10 caracteres,
de uma estação metereológica, a principio esse codigo deve trazer os seguintes dados:
zona de medição = 02 caracteres ==> 01 sul 02 norte 03 leste 04 oeste
temperatura     = 04 caracteres ==> 0321 ==> temperatura + 32,1ºC ou 1321 temperatura -32,1ºC
pluviometria    = 04 caracteres ==> 0400 ==> indice pluviometrio 400mm 
Exemplo se o código recebido for 0402980010 seu software deve decodificar a seguinte informação:
Campinas, região:Norte,  Temperatura: 29,8ºC, Indice pluviométrico:10mm 
Não permita que seja digitado um código de menos de 10 caracteres e que não seja um numero
decimal

5) Escreva um programa para aprovar  o empréstimo bancário para compra de uma casa. O programa
deve perguntar o valor da casa, o salário, e a quantidade de anos a pagar. O valor da prestação 
mensal não pode ser maior que 30% do sálario. Calcule o valor da prestação como sendo o valor 
da casa dividido pelo numero de meses a pagar. Não permita o empréstimo se a condição citada 
não for atendida. 
Não permita a entrada de valores que não sejam numeros.

link para respostas==> https://forms.gle/QhFNCdQ3QTJ2Jdtc9
'''