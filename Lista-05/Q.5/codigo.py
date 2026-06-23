vetor = []
for i in range(10, 21):
    vetor.append(i)

tamanho = len(vetor)
for i in range(tamanho - 1, -1, -1):
    if vetor[i] % 2 == 0:
        print(vetor[i])