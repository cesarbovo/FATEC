# Exercício 5: Comparação de dois números

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("O primeiro número é maior")
elif num2 > num1:
    print("O segundo número é maior")
else:
    print("Os números são iguais")