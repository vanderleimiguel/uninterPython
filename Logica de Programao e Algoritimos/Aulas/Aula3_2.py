kwh = float(input("Quantos kwh? "))
tipo = input("Qual o tipo de instalacao (R, C OU I)? ")

if tipo == "R":
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif tipo == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif tipo == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print("Instalacao invalida")

print("Total a pagar: {}".format(kwh * preco))
