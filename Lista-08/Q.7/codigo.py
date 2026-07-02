def permutar(texto, resposta=""):
    if len(texto) == 0:
        print(resposta)
        return
    for i in range(len(texto)):
        caractere = texto[i]
        resto = texto[:i] + texto[i+1:]
        permutar(resto, resposta + caractere)

palavra = input("Digite a palavra para permutar: ")
permutar(palavra)
