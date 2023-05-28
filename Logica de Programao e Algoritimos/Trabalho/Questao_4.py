# Questao 4 de 4
# Aluno: Vanderlei do Nascimento Miguel Junior
# RU: 4502606

# ---------- Inicio das Variaveis Globais ---------
listaPeca = []
codigoPeca = 0

# ---------- Fim das Variaveis Globais ---------


# inicio funcao cadastrarPeca()
def cadastrarPeca(codigo):
    print("Voce selecionou a opcao de cadastrar peca")
    print("Codigo da peca {}".format(codigo))
    nome = input("Por favor entre com o NOME da peca: ")
    fabricante = input("Por favor entre com o FABRICANTE da peca: ")
    valor = int(input("Por favor entre com o VALOR(R$) da peca: "))

    dicionarioPeca = {
        "codigo": codigo,
        "nome": nome,
        "fabricante": fabricante,
        "valor": valor,
    }
    listaPeca.append(dicionarioPeca.copy())


# fim da funcao cadastrarPeca()


# inicio funcao consultarPeca()
def consultarPeca():
    print("Voce selecionou a opcao de consultar peca")
    while True:
        opcaoConsultar = input(
            "\nEscolha a opcao desejada:\n"
            + "1-Consultar Todas as Pecas\n"
            + "2-Consultar Pecas por Codigo\n"
            + "3-Consultar Pecas por Fabricante\n"
            + "4-Retornar\n"
            + ">>"
        )
        if opcaoConsultar == "1":
            print("Voce escolheu a opcao consultar todas as pecas")
            for peca in listaPeca:  # peca vai varrer lista
                print("------------------")
                for (
                    key,
                    value,
                ) in (
                    peca.items()
                ):  # varrer todos os conjuntos chave e valor dos dicionarios
                    print("{}: {}".format(key, value))
                print("------------------")
        elif opcaoConsultar == "2":
            print("Voce escolheu a opcao consultar pecas po codigo")
            valorDesejado = int(input("Entre com o codigo desejado: "))
            for peca in listaPeca:
                if peca["codigo"] == valorDesejado:
                    print("------------------")
                    for (
                        key,
                        value,
                    ) in (
                        peca.items()
                    ):  # varrer todos os conjuntos chave e valor dos dicionarios
                        print("{}: {}".format(key, value))
                    print("------------------")
        elif opcaoConsultar == "3":
            print("Voce escolheu a opcao consultar pecas por fabricante")
            valorDesejado = input("Entre com o fabricante desejado: ")
            for peca in listaPeca:
                if peca["fabricante"] == valorDesejado:
                    print("------------------")
                    for (
                        key,
                        value,
                    ) in (
                        peca.items()
                    ):  # varrer todos os conjuntos chave e valor dos dicionarios
                        print("{}: {}".format(key, value))
                    print("------------------")
        elif opcaoConsultar == "4":
            return
        else:
            print("Opcao invalida")
            continue


# fim da funcao consultarPeca()


# inicio funcao removerPeca()
def removerPeca():
    print("Voce selecionou a opcao de remover peca")
    valorDesejado = int(input("Entre com o codigo que deseja remover: "))
    for peca in listaPeca:
        if peca["codigo"] == valorDesejado:
            listaPeca.remove(peca)
            print("Peca removida")


# fim da funcao removerPeca()

# inicio do Main
print(
    "Bem vindo ao Controle de Estoque da Bicicletaria do Vanderlei do Nasc. Miguel Jr"
)
while True:
    opcaoPrincipal = input(
        "\nEscolha a opcao desejada:\n"
        + "1-Cadastrar Pecas\n"
        + "2-Consultar Pecas\n"
        + "3-Remover Pecas\n"
        + "4-Sair\n"
        + ">>"
    )
    if opcaoPrincipal == "1":
        codigoPeca = codigoPeca + 1
        cadastrarPeca(codigoPeca)
    elif opcaoPrincipal == "2":
        consultarPeca()
    elif opcaoPrincipal == "3":
        removerPeca()
    elif opcaoPrincipal == "4":
        break  # encerra laco
    else:
        print("Opcao invalida")
        continue  # volta para inicio
# Fim do Main
