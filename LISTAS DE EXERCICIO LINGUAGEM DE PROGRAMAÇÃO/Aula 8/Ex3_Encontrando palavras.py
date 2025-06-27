# Exercício 3 - Encontrando palavras

frase = input("Digite uma frase: ")
palavra = input("Qual palavra deseja procurar? ")

if palavra in frase:
    posicao = frase.find(palavra)
    print(f"A palavra '{palavra}' foi encontrada na posição {posicao}.")
else:
    print(f"A palavra '{palavra}' não foi encontrada na frase.")
