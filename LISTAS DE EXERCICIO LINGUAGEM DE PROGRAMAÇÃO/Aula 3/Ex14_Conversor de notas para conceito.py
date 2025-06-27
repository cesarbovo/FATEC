# Exercício 14: Conversor de notas para conceito

nota = float(input("Digite a nota (0-10): "))
if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
elif nota >= 3:
    print("D")
else:
    print("E")