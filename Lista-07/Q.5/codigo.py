def calcImc(altura,peso):
    imc = peso/altura**2
    if(imc<18.5):
        classificacao = "Magreza"
        grauObesidade = "0"
    elif(18.5<=imc<=24.9):
        classificacao = "Normal"
        grauObesidade = "0"
    elif(25.0<=imc<=29.9):
        classificacao = "Sobrepeso"
        grauObesidade = "I"
    elif(30.0<=imc<=39.9):
        classificacao = "Obesidade"
        grauObesidade = "II"
    else:
        classificacao = "Obesidade Grave"
        grauObesidade = "III"
        
    return imc, classificacao, grauObesidade

meu_peso = float(input("Digite seu peso (kg): "))
minha_altura = float(input("Digite sua altura (m): "))

resultado, classe, grau = calcImc(minha_altura, meu_peso)

print(f"Seu IMC é: {resultado:.2f}")
print(f"Classificação: {classe}")
print(f"Obesidade (Grau): {grau}")