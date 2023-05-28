# Rodar programa
# no terminal digitar python nome do fonte

nome = input("Qual seu nome? ")
print("Olá {}, seja Bem-Vindo!".format(nome))

nota1 = float(input("Qual nota voce recebeu na disciplina 1?"))
nota2 = float(input("Qual nota voce recebeu na disciplina 2?"))
print(
    "Olá {}, voce tirou {} na disciplina 1 e {} na disciplina 2!".format(
        nome, nota1, nota2
    )
)
print("Sua média foi {}".format((nota1 + nota2) / 2))
