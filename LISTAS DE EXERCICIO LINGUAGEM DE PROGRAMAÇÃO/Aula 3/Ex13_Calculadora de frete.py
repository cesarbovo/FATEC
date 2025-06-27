# Exercício 13: Calculadora de frete

valor = float(input("Digite o valor da compra: "))
if valor > 100:
    print("Frete grátis")
else:
    print("Frete: R$ 15,00")