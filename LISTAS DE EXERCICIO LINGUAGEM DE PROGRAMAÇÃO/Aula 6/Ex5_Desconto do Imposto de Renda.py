# Exercício 5: Desconto do imposto de renda

salario = float(input("Informe seu salário bruto (R$): "))

# Cálculo do IR com base nas faixas
if salario <= 2112.00:
    print("Isento de Imposto de Renda. Não há imposto a pagar.")
elif salario <= 2826.65:
    aliquota = 0.075
    deducao = 158.40
    imposto = (salario * aliquota) - deducao
    print(f"Alíquota: 7,5%")
    print(f"Imposto de Renda a pagar: R$ {imposto:.2f}")
elif salario <= 3751.05:
    aliquota = 0.15
    deducao = 370.40
    imposto = (salario * aliquota) - deducao
    print(f"Alíquota: 15%")
    print(f"Imposto de Renda a pagar: R$ {imposto:.2f}")
elif salario <= 4664.68:
    aliquota = 0.225
    deducao = 651.73
    imposto = (salario * aliquota) - deducao
    print(f"Alíquota: 22,5%")
    print(f"Imposto de Renda a pagar: R$ {imposto:.2f}")
else:
    aliquota = 0.275
    deducao = 884.96
    imposto = (salario * aliquota) - deducao
    print(f"Alíquota: 27,5%")
    print(f"Imposto de Renda a pagar: R$ {imposto:.2f}")
