# Exercício 14 - Inteiros para Romanos

def int_para_romano(n):
    mapa = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    romano = ""
    for valor, simbolo in mapa:
        while n >= valor:
            romano += simbolo
            n -= valor
    return romano

# Testes
for numero in [3, 9, 58, 1994, 2025]:
    print(f"{numero} -> {int_para_romano(numero)}")
