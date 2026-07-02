def maior_recursivo(vetor, n):
    if n == 1:
        return vetor[0]
    sub_maior = maior_recursivo(vetor, n - 1)
    if vetor[n - 1] > sub_maior:
        return vetor[n - 1]
    return sub_maior

vetor = []
for i in range(10):
    vetor.append(int(input(f"Vetor [{i}]: ")))

print("Maior valor:", maior_recursivo(vetor, 10))
