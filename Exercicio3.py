frase = input("Digite uma frase: ")
tamFrase = len(frase)

frase2 = frase[: int(tamFrase / 2)]
print(frase2[-2:])
