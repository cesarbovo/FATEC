# Exercício 11: Jogo de adivinhação

import random
numero_secreto = random.randint(1, 100)
tentativa = int(input("Adivinhe o número (1-100): "))

if tentativa > numero_secreto:
    print("Muito alto!")
elif tentativa < numero_secreto:
    print("Muito baixo!")
else:
    print("Parabéns!")