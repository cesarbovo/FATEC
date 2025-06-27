# Exercício 6 - Tupla de tuplas

carrinho = (
    ("Arroz", 24.90),
    ("Feijão", 8.50),
    ("Leite", 4.80),
)

for nome, preco in carrinho:
    print(f"Produto: {nome} | Preço: R$ {preco:.2f}")
