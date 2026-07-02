def exponencial(n):
    if n == 0:
        return 1
    return 2 * exponencial(n - 1)

num = int(input("Digite o valor de n: "))
print(f"2^{num} =", exponencial(num))
