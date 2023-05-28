# Questao 2 de 4
# Aluno: Vanderlei do Nascimento Miguel Junior
# RU: 4502606

print("Bem vindo a Lanchonete do Vanderlei do Nasc. Miguel Jr")
print("***************** Cardapio ***************")
print("| Codigo |       Descricao       |   Valor |")
print("|   100  |     Cachorro Quente   |    9,00 |")
print("|   101  | Carrocho Quente Duplo |   11,00 |")
print("|   102  |        X-Egg          |   12,00 |")
print("|   103  |       X-Salada        |   12,00 |")
print("|   104  |        X-Bacon        |   14,00 |")
print("|   105  |        X-Tudo         |   17,00 |")
print("|   200  |    Refrigerante Lata  |    5,00 |")
print("|   201  |      Cha Gelado       |    4,00 |")

acumulador = 0

while True:
    codigo = int(
        input("Entre com o codigo desejado (100/101/102/103/104/105/200/201): ")
    )
    if (
        codigo != 100
        and codigo != 101
        and codigo != 102
        and codigo != 103
        and codigo != 104
        and codigo != 105
        and codigo != 200
        and codigo != 201
    ):
        print("Opcao Invalida")
        continue  # volta para o inicio do while
    if codigo == 100:
        print("Voce escolheu o cachorro quente no valor de R$ 9,00")
        acumulador = acumulador + 9
    elif codigo == 101:
        print("Voce escolheu o cachorro quente duplo no valor de R$ 11,00")
        acumulador = acumulador + 11
    elif codigo == 102:
        print("Voce escolheu o X-Egg no valor de R$ 12,00")
        acumulador = acumulador + 12
    elif codigo == 103:
        print("Voce escolheu o X-Salada no valor de R$ 12,00")
        acumulador = acumulador + 12
    elif codigo == 104:
        print("Voce escolheu o X-Bacon no valor de R$ 14,00")
        acumulador = acumulador + 14
    elif codigo == 105:
        print("Voce escolheu o X-Tudo no valor de R$ 17,00")
        acumulador = acumulador + 17
    elif codigo == 200:
        print("Voce escolheu o refrigerante lata no valor de R$ 5,00")
        acumulador = acumulador + 5
    elif codigo == 201:
        print("Voce escolheu o Cha gelado no valor de R$ 4,00")
        acumulador = acumulador + 4

    pedir_mais = int(input("Deseja pedir mais alguma coisa?\n" "1 - Sim\n" "2 - Nao\n"))
    if pedir_mais == 1:
        continue
    else:
        print("O valor total a ser pago: R$ {:.2f}".format(acumulador))
        break
