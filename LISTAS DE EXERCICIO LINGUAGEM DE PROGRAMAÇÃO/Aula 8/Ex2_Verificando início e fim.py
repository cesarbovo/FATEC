# Exercício 2 - Verificando início e fim

frase = input("Digite uma frase: ")

if frase.startswith("Bom dia"):
    print("A frase começa com 'Bom dia'.")
else:
    print("A frase não começa com 'Bom dia'.")

if frase.endswith("obrigado"):
    print("A frase termina com 'obrigado'.")
else:
    print("A frase não termina com 'obrigado'.")
