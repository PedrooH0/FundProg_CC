import random

vetor = []
for i in range(10):
    vetor.append(random.randint(1, 15))

repetidos = []
for i in range(10):
    for j in range(i + 1, 10):
        if vetor[i] == vetor[j]:
            ja_existe = False
            for x in repetidos:
                if x == vetor[i]:
                    ja_existe = True
            if not ja_existe:
                repetidos.append(vetor[i])

print(vetor)
print("Quantidade de números repitidos: ",len(repetidos))
if len(repetidos) > 0:
    print(repetidos)
