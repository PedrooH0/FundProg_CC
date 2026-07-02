def inverter(texto):
    if len(texto) <= 1:
        return texto
    return texto[-1] + inverter(texto[:-1])

palavra = input("Digite uma palavra: ")
print("Palavra invertida: ", inverter(palavra))
