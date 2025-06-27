# Exercício 12: Classificação de temperaturas

temp = float(input("Digite a temperatura em Celsius: "))
if temp <= 15:
    print("Frio")
elif temp <= 25:
    print("Agradável")
else:
    print("Quente")