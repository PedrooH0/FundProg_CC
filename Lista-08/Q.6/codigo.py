def soma_num(n):
    if n == 1:
        return 1
    return n + soma_num(n - 1)

num = int(input("Digite um número: "))
print(f"Soma dos numéros de 1 até {num}: ", soma_num(num))
