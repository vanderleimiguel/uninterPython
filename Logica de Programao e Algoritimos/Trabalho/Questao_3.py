# Questao 3 de 4
# Aluno: Vanderlei do Nascimento Miguel Junior
# RU: 4502606


# inicio funcao dimensoesObjeto()
def dimensoesObjeto():
    while True:
        try:
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
        except ValueError:
            print("Voce digitou alguma dimensao do objeto com valor não numerico")
            print("Por favor entre com as dimensoes novamente")
            continue
        try:
            largura = float(input("Digite a largura do objeto (em cm): "))
        except ValueError:
            print("Voce digitou alguma dimensao do objeto com valor não numerico")
            print("Por favor entre com as dimensoes novamente")
            continue
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
        except ValueError:
            print("Voce digitou alguma dimensao do objeto com valor não numerico")
            print("Por favor entre com as dimensoes novamente")
            continue

        volume = comprimento * largura * altura
        print("O volume do objeto é {}".format(volume))

        if volume < 1000:
            valor = 10
        elif volume >= 1000 and volume < 10000:
            valor = 20
        elif volume >= 10000 and volume < 30000:
            valor = 30
        elif volume >= 30000 and volume < 100000:
            valor = 50
        else:
            print("não aceitamos objetos com dimensoes ao grandes!")
            print("entre com as dimensoes novamente!")
            continue

        return valor


# fim da funcao dimensoesObjeto()


# inicio funcao pesoObjeto()
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
        except ValueError:
            print("Voce digitou peso do objeto com valor nao numerico")
            print("Por favor entre com o peso novamente")
            continue

        if peso <= 0.1:
            multiplicador = 1
        elif peso >= 0.1 and peso < 1:
            multiplicador = 1.5
        elif peso >= 1 and peso < 10:
            multiplicador = 2
        elif peso >= 10 and peso < 30:
            multiplicador = 3
        else:
            print("não aceitamos objetos tão pesados!")
            print("entre com o peso novamente!")
            continue

        return multiplicador


# fim da funcao pesoObjeto()


# inicio funcao rotaObjeto()
def rotaObjeto():
    while True:
        print("***************** Rotas ****************")
        print("| RS | De Rio de Janeiro até São Paulo |")
        print("| BS | De Brasilia até São Paulo       |")
        print("| BR | De Brasilia até Rio de Janeiro  |")
        rota = input("Selecione a Rota: ").upper()
        if rota != "RS" and rota != "BS" and rota != "BR":
            print(
                "Voce digitou uma rota que não existe!\n"
                "Por favor entre com a rota novamente!"
            )
            continue

        if rota == "RS":
            multiplRota = 1
        elif rota == "BS":
            multiplRota = 1.2
        else:
            multiplRota = 1.5

        return multiplRota


# fim da funcao rotaObjeto()

# inicio do Main
print("Bem vindo a Companhia de logistica do Vanderlei do Nasc. Miguel Jr")
valorDimensao = dimensoesObjeto()
valorPeso = pesoObjeto()
valorRota = rotaObjeto()

total = valorDimensao * valorPeso * valorRota
print(
    "Total a pagar (R$): {:.2f} (dimensões: {} * peso: {} * rota: {}".format(
        total, valorDimensao, valorPeso, valorRota
    )
)
