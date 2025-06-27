# Exercício 16: Cálculo de imposto de renda

salario = float(input("Digite o salário bruto: "))
if salario <= 1900:
    imposto = 0
elif salario <= 2800:
    imposto = salario * 0.075
elif salario <= 3700:
    imposto = salario * 0.15
elif salario <= 4600:
    imposto = salario * 0.225
else:
    imposto = salario * 0.275

print(f"Imposto devido: R$ {imposto:.2f}")