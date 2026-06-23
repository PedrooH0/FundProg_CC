import random

vetor = []
for i in range(10):
    vetor.append(random.randint(1, 100))

primos = []
for num in vetor:
    if num > 1:
        e_primo = True
        for i in range(2, num):
            if num % i == 0:
                e_primo = False
                break
        if e_primo:
            primos.append(num)

print("Número de números primos: ",len(primos))
print(primos)
