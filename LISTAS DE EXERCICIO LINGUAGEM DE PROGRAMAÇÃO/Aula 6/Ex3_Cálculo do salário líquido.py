'''
Uma empresa deseja calcular o salario liquido de seus funcionarios com base em seus cargos, 
levando em consideração beneficios e descontos de impostos.

Salario liquido = Salario base + Beneficios - Impostos
'''

# Dicionário com os dados dos cargos
cargos = {
    1: {"cargo": "Escriturário", "salario_base": 2500.00, "beneficios": 300.00, "imposto": 0.08},
    2: {"cargo": "Secretário", "salario_base": 3200.00, "beneficios": 450.00, "imposto": 0.10},
    3: {"cargo": "Caixa", "salario_base": 3800.00, "beneficios": 600.00, "imposto": 0.12},
    4: {"cargo": "Gerente", "salario_base": 7500.00, "beneficios": 1000.00, "imposto": 0.15},
    5: {"cargo": "Diretor", "salario_base": 12000.00, "beneficios": 2000.00, "imposto": 0.20}
}

# Solicita ao usuário o código do cargo
codigo = int(input("Informe o código do cargo (1 a 5): "))

# Verifica se o código existe no dicionário
if codigo in cargos:
    cargo_info = cargos[codigo]
    salario_base = cargo_info["salario_base"]
    beneficios = cargo_info["beneficios"]
    imposto = cargo_info["imposto"]

    # Cálculo do salário líquido
    salario_liquido = salario_base + beneficios - (salario_base * imposto)

    # Exibe o resultado formatado
    print(f"\nCargo: {cargo_info['cargo']}")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Benefícios: R$ {beneficios:.2f}")
    print(f"Imposto: {imposto*100:.0f}%")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
else:
    print("Código de cargo inválido. Por favor, informe um código entre 1 e 5.")