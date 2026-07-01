def conceitovalor(valor):
    if(0<=valor<=4.9):
        return "Conceito D"
    elif(5<=valor<=6.9):
        return "Conceito C"
    elif(7<=valor<=8.9):
        return "Conceito B"
    elif(9<=valor<=10):
        return "Conceito A"

media = float(input("Digite a sua média: "))
resultado = conceitovalor(media)
print(resultado)
