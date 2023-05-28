# Questao 1 de 4
# Aluno: Vanderlei do Nascimento Miguel Junior
# RU: 4502606

print("Bem vindo a Loja do Vanderlei do Nasc. Miguel Jr")
valor = float(input("Entre com o valor do produto: "))
qtd = int(input("Entre com o valor da quantidade: "))

if qtd <= 9:
    desconto = 0.00
elif qtd >= 10 and qtd <= 99:
    desconto = 0.05
elif qtd >= 100 and qtd <= 999:
    desconto = 0.10
else:
    desconto = 0.15

total_sem_desc = valor * qtd

print("O valor SEM desconto foi: R$ {:.2f}".format(total_sem_desc))
if desconto != 0.00:
    print("Seu desconto foi de {}%".format(100 * desconto))
    print(
        "O valor COM desconto foi: R$ {:.2f}".format(
            (total_sem_desc - (total_sem_desc * desconto))
        )
    )
