matriz = []

for i in range(12):
    posicao = int(input(f"Posição do {i+1}º time: "))
    nome = input("Nome do time: ")
    pontos = int(input("Pontos: "))
    jogos = int(input("Jogos: "))
    vitorias = int(input("Vitórias: "))
    empates = int(input("Empates: "))
    derrotas = int(input("Derrotas: "))
    
    linha = [posicao, nome, pontos, jogos, vitorias, empates, derrotas]
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(i + 1, len(matriz)):
        if matriz[i][0] > matriz[j][0]:
            matriz[i], matriz[j] = matriz[j], matriz[i]

print("\nCampeão brasileiro:")
print(matriz[0][1])

print("\nClassificados para a Libertadores:")
for i in range(5):
    print(matriz[i][1])

print("\nClassificados para a Sul-Americana:")
for i in range(5, 10):
    print(matriz[i][1])

print("\nRebaixados para a série B:")
for i in range(10, 12):
    print(matriz[i][1])