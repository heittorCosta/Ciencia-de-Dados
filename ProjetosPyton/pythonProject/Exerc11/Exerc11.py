nome = input("Digite seu nome")
sexo = input("Digite M para masculino ou F para feminino")

if sexo in ("M" or "F"):
    if sexo == "M":
        print("IImo. Sr ", nome)
    else:
        print("IIma. Sra. ", nome)
else:
    print("Sexo informado Inválido!")