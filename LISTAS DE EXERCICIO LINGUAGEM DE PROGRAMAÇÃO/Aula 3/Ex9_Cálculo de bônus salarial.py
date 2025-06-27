# Exercício 9: Cálculo de bônus salarial

salario = float(input("Digite seu salário: "))
if salario < 2000:
    bonus = salario * 0.2
elif salario <= 5000:
    bonus = salario * 0.1
else:
    bonus = salario * 0.05

print(f"Bônus: R$ {bonus:.2f}")