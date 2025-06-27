# Exercício 9 - Interação sobre dicionário

compras = {
    "Sabonete": 2.50,
    "Shampoo": 15.00,
    "Condicionador": 16.50
}

for item, preco in compras.items():
    print(f"{item}: R$ {preco:.2f}")
