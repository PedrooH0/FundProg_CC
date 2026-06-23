import random

vetor = []
for i in range(10):
    vetor.append(random.randint(1, 20))

print(vetor)
valor = int(input("Digite um número: "))
posicao = -1

for i in range(10):
    if vetor[i] == valor:
        posicao = i
        break

if(posicao==-1):
    print("Esse número não está na lista")
else:
    print(posicao)