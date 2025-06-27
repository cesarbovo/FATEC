# Exercício 11 - Top 3 Sum

numeros = [10, 3, 5, 7, 2, 8, 12]
numeros.sort()
soma_menores = sum(numeros[:3])
soma_maiores = sum(numeros[-3:])
print(soma_menores, soma_maiores)
