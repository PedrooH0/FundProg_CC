fibonacci = [0, 1]
for i in range(18):
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

print(fibonacci)