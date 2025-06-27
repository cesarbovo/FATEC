#Exercício 4: Idade para entrada na festa

idade = int(input("Digite sua idade: "))

# Verificação para entrar na festa
if idade < 14:
    entrada = "Não pode entrar"
elif idade < 18:
    entrada = "Pode com acompanhamento dos pais"
else:
    entrada = "Pode entrar"

# Verificação para beber
if idade < 18:
    bebida = "Não pode beber"
else:
    bebida = "Pode beber"

print("\n--- Resultado ---")
print(f"Idade: {idade} anos")
print(f"Condição para entrar na festa: {entrada}")
print(f"Condição para beber: {bebida}")
