# Exercício 4: Desconto no ingresso

idade = int(input("Digite sua idade: "))
if idade < 12 or idade > 60:
    print("Ingresso custa R$ 15,00")
else:
    print("Ingresso custa R$ 30,00")