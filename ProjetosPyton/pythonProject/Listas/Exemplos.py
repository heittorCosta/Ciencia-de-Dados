# #Cálculo de média
# notas = [6,8,10,7,9]
# soma = 0
# x = 0
#
# while x<5:
#     soma += notas[x]
#     x = x + 1
#
# print("Média: %5.2f" % (soma/x))

# notas = [0,0,0,0,0]
# soma = 0
# x = 0
#
# while x<5:
#     notas[x] = float(input("Nota %d:" % x))
#     soma += notas[x]
#     x = x + 1
#
# x = 0
#
# while x<5:
#     print("Nota %d: %6.2f" % (x, notas[x]))
#     x = x + 1
#
# print("Média: %5.2f" % (soma/x))


#APRESENTAÇÃO DE NÚMEROS
# l = [1,2,3]
# x = 0
# while x < len(l):
#     print(l[x])
#     x+=1
#
# l.append(4)
# print(l)
#
# l = []
# while True:
#     n = int(input("Digite um número (0 para sair):"))
#     if n == 0:
#         break
#     l.append(n)
#
# x = 0
# while x< len(l):
#     print(l[x])
#     x = x + 1
#


# l = list(range(101))
# l.pop()
# print(l)
# del l[1:99]
# print(l)

# ultimo = 10
# fila = list(range(1,ultimo+1))
# while True:
#     print("\nExistem %d clientes na fila" % len(fila))
#     print("Fila Atual:", fila)
#     print("Digite F para adicionar um cliente ao fim da fila")
#     print("ou A para realizar o atendimento. S para sair.")
#     operacao = input("Operação (F, A ou S)")
#
#     if operacao == "A":
#         if (len(fila))>0:
#             atendimento = fila.pop(0)
#             print("Cliente %d atendido" % atendimento)
#         else:
#             print("Fila vazia, ninguém para atender")
#     elif operacao == "F":
#         ultimo+=1
#         fila.append(ultimo)
#     elif operacao == "S":
#         break
#     else:
#         print("Operação inválida digite apenas A, F ou S")

# prato = 5
# pilha = list(range(1,prato+1))
# while True:
#     print("\nExistem %d pratos na pilha" % len(pilha))
#     print("Pilha Atual:", pilha)
#     print("Digite E para empilhar um novo prato")
#     print("ou D para desempilhar. S para sair.")
#     operacao = input("Operação (E, D ou S)")
#
#     if operacao == "D":
#         if (len(pilha))>0:
#             atendimento = pilha.pop()
#             print("Cliente %d atendido" % atendimento)
#         else:
#             print("Fila vazia, ninguém para atender")
#     elif operacao == "E":
#         prato+=1
#         pilha.append(prato)
#     elif operacao == "S":
#         break
#     else:
#         print("Operação inválida digite apenas E, D ou S")

l = [15,7,27,39]
p = int(input("Digite o valor a procurar."))
achou = False
x = 0

while x<len(l):
    if l[x] == p:
        achou = True
        break
    x+=1

if achou:
    print("%d achado na posição %d" %(p,x))
else:
    print("%d não encontrado" %p)