# Exercício 1 - Contando Palavras

frase = input("Digite uma frase: ")

# Converte tudo para minúsculas e conta quantas vezes "python" aparece
quantidade = frase.lower().count("python")

print(f'A palavra "Python" aparece {quantidade} vez(es) na frase.')
