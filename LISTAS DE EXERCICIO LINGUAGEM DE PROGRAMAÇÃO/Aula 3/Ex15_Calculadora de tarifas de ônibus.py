# Exercício 15: Calculadora de tarifas de ônibus

idade = int(input("Digite sua idade: "))
estudante = input("Tem cartão estudante? (S/N): ").upper()

if idade < 6 or idade > 65:
    print("Grátis")
elif estudante == 'S':
    print("50% de desconto")
else:
    print("Tarifa normal")