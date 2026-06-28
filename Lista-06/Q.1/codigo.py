matriz = []

for i in range(5):
    conta = input("Informe o número da conta: ")
    nome = input("Informe o nome do Cliente: ")
    saldo_inicial = float(input("Informe o saldo atual: "))
    op = input("Escolha um tipo de operação (C = Crédito / D = Débito): ").upper()
    valor_movimentacao = float(input("Digite o valor movimentado: "))

    if op == "C":
        saldo_atualizado = saldo_inicial + valor_movimentacao
    elif op == "D":
        saldo_atualizado = saldo_inicial - valor_movimentacao
    else:
        saldo_atualizado = saldo_inicial

    linha = [conta, nome, saldo_inicial, op, saldo_atualizado]
    matriz.append(linha)

for linha in matriz:
    print(linha)
