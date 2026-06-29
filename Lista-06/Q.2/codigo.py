matriz = []

for i in range(4):
    matricula = input("Informe sua matrícula: ")
    nome = input("Informe o seu nome: ")
    funcao = input("Informe sua função: ")
    salario = float(input("Informe seu salário: "))
    print("")
    
    linha = [matricula, nome, funcao, salario]
    matriz.append(linha)

print("\nResultado da Análise Salarial")
for linha in matriz:
    print(linha)

maior_salario = matriz[0][3]
funcionario_maior = matriz[0]

menor_salario = matriz[0][3]
funcionario_menor = matriz[0]


for funcionario in matriz:
    
    if funcionario[3] > maior_salario:
        maior_salario = funcionario[3]
        funcionario_maior = funcionario
        
    if funcionario[3] < menor_salario:
        menor_salario = funcionario[3]
        funcionario_menor = funcionario

print("\nResultado da Análise Salarial")
print(f"Maior Salário: R$ {funcionario_maior[3]:.2f} - Funcionário: {funcionario_maior[1]}")
print(f"Menor Salário: R$ {funcionario_menor[3]:.2f} - Funcionário: {funcionario_menor[1]}")