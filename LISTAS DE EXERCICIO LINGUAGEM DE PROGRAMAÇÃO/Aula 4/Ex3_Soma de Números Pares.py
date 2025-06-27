# Exercício 3: Soma de Números Pares

n = int(input("Digite um número: "))
soma = 0

for i in range(2, n + 1, 2):
    soma += i

print(f"A soma dos números pares de 1 até {n} é: {soma}")
