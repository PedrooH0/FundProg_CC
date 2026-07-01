def sacar(valor):
    valor_original = valor
    
    if valor == 1 or valor == 3 or valor < 0:
        print(f"Não é possível sacar R$ {valor}.")
        return

    notas_200 = 0
    notas_100 = 0
    notas_50 = 0
    notas_20 = 0
    notas_5 = 0
    notas_2 = 0

    if valor % 2 != 0:
        notas_5 = 1
        valor = valor - 5

    notas_200 = valor // 200
    valor = valor % 200

    notas_100 = valor // 100
    valor = valor % 100

    notas_50 = valor // 50
    valor = valor % 50

    if valor == 10 or valor == 30:
        notas_5 = notas_5 + 2
        valor = valor - 10

    notas_20 = valor // 20
    valor = valor % 20

    notas_2 = valor // 2

    total_notas = notas_200 + notas_100 + notas_50 + notas_20 + notas_5 + notas_2
    
    print(f"Para sacar {valor_original} reais, serão necessárias {total_notas} cédulas:")
    if notas_200 > 0: print(f"- {notas_200} nota(s) de R$ 200")
    if notas_100 > 0: print(f"- {notas_100} nota(s) de R$ 100")
    if notas_50 > 0:  print(f"- {notas_50} nota(s) de R$ 50")
    if notas_20 > 0:  print(f"- {notas_20} nota(s) de R$ 20")
    if notas_5 > 0:   print(f"- {notas_5} nota(s) de R$ 5")
    if notas_2 > 0:   print(f"- {notas_2} nota(s) de R$ 2")

valor_usuario = int(input("Digite o valor que deseja sacar: "))
sacar(valor_usuario)
