vetor1 = []
for i in range(2, 21):
    if i % 2 == 0:
        vetor1.append(i * i)

vetor2 = []
for i in range(10, 20):
    vetor2.append(i)

soma = []
for i in range(10):
    soma.append(vetor1[i] + vetor2[i])

print(soma)
