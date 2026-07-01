def informar_matriz(matriz):
    soma_l0 = sum(matriz[0])
    soma_l1 = sum(matriz[1])
    soma_l2 = sum(matriz[2])

    menor_soma_linha = soma_l0
    linha_menor = 0

    if soma_l1 < menor_soma_linha:
        menor_soma_linha = soma_l1
        linha_menor = 1
    if soma_l2 < menor_soma_linha:
        menor_soma_linha = soma_l2
        linha_menor = 2

    soma_c0 = matriz[0][0] + matriz[1][0] + matriz[2][0]
    soma_c1 = matriz[0][1] + matriz[1][1] + matriz[2][1]
    soma_c2 = matriz[0][2] + matriz[1][2] + matriz[2][2]

    maior_soma_coluna = soma_c0
    coluna_maior = 0

    if soma_c1 > maior_soma_coluna:
        maior_soma_coluna = soma_c1
        coluna_maior = 1
    if soma_c2 > maior_soma_coluna:
        maior_soma_coluna = soma_c2
        coluna_maior = 2

    print(f"Coluna com maior valor: {coluna_maior} (Soma: {maior_soma_coluna})")
    print(f"Linha com menor valor: {linha_menor} (Soma: {menor_soma_linha})")

minha_matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    minha_matriz.append(linha)

informar_matriz(minha_matriz)
