def soma_diagonal():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(int(input(f"Matriz [{i}][{j}]: ")))
        matriz.append(linha)
    
    soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
    return soma

print("Soma da diagonal:", soma_diagonal())
