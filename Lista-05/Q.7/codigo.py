import random

vetor = []
for i in range(10):
    vetor.append(random.randint(1, 100))

pares = 0
impares = 0

for num in vetor:
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(vetor)
print("Pares: ",pares)
print("Ímpares: ",impares)
