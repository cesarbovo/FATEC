# Exercício 17: Simulação de saque bancário

valor = int(input("Digite o valor do saque: "))
notas100 = valor // 100
resto = valor % 100
notas50 = resto // 50
resto = resto % 50
notas20 = resto // 20
resto = resto % 20
notas10 = resto // 10

print(f"Notas de R$100: {notas100}")
print(f"Notas de R$50: {notas50}")
print(f"Notas de R$20: {notas20}")
print(f"Notas de R$10: {notas10}")