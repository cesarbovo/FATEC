# Exercício 10 - Mini-Max Sum

numeros = [1, 3, 5, 7, 9]
numeros.sort()
min_soma = sum(numeros[:4])
max_soma = sum(numeros[-4:])
print(min_soma, max_soma)
