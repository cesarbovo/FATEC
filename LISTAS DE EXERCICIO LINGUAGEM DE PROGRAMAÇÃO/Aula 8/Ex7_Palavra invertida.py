# Exercício 7 - Palavra invertida

palavra = input("Digite uma palavra: ")
invertida = palavra[::-1]

print("Palavra invertida:", invertida)

if palavra.lower() == invertida.lower():
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
