# Exercício 8 - Adição e atualização

tabela = {
    "Arroz": 24.90,
    "Feijão": 8.50,
    "Leite": 4.80,
    "Açúcar": 3.90
}

# Adiciona novo item
tabela["Café"] = 14.20

# Atualiza item existente
tabela["Açúcar"] = 4.10

# Exibe dicionário atualizado
print("Tabela atualizada:")
for produto, preco in tabela.items():
    print(f"{produto}: R$ {preco:.2f}")
