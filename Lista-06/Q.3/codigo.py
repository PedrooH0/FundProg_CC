import random

N = 3
matriz = []

for i in range(N):
    linha = []
    for j in range(N):
        linha.append(random.randint(0, 10))
    matriz.append(linha)


print("--- Valores da Matriz ---")
for linha in matriz:
    print(linha)
print("-" * 25)

soma_referencia = sum(matriz[0])
eh_quadrado_magico = True


for i in range(N):
    if sum(matriz[i]) != soma_referencia:
        eh_quadrado_magico = False


for j in range(N):
    soma_coluna = 0
    for i in range(N):
        soma_coluna += matriz[i][j]
    if soma_coluna != soma_referencia:
        eh_quadrado_magico = False


soma_diagonal_principal = 0
for i in range(N):
    soma_diagonal_principal += matriz[i][i]
if soma_diagonal_principal != soma_referencia:
    eh_quadrado_magico = False


soma_diagonal_secundaria = 0
for i in range(N):
    soma_diagonal_secundaria += matriz[i][N - 1 - i]
if soma_diagonal_secundaria != soma_referencia:
    eh_quadrado_magico = False


if eh_quadrado_magico:
    print("É uma matriz QUADRADO MÁGICO")
else:
    print("NÃO é uma matriz QUADRADO MÁGICO")