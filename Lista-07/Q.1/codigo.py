from datetime import datetime

def calcular_dias(data_texto):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    partes = data_texto.lower().split(" de ")
    
    dia = int(partes[0])
    mes = meses.index(partes[1]) + 1
    ano = int(partes[2])
    
    data_passada = datetime(ano, mes, dia)
    hoje = datetime.now()
    
    return (hoje - data_passada).days

entrada = input("Digite uma data válida (ex: 20 de Janeiro de 2025): ")
resultado = calcular_dias(entrada)
print(resultado)
