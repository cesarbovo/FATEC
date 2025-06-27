# Exercício 5: Cálculo do Fatorial

n = int(input("Digite um número para calcular o fatorial: "))

# Validação
if n < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Usando for
    fatorial_for = 1
    for i in range(1, n + 1):
        fatorial_for *= i

    # Usando while
    fatorial_while = 1
    i = 1
    while i <= n:
        fatorial_while *= i
        i += 1

    print(f"Usando for: {n}! = {fatorial_for}")
    print(f"Usando while: {n}! = {fatorial_while}")
