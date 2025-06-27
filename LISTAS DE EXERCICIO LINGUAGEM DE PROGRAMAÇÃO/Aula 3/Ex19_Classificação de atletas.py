# Exercício 19: Classificação de atletas

idade = int(input("Digite a idade do atleta: "))
if idade <= 12:
    print("Infantil")
elif idade <= 17:
    print("Juvenil")
elif idade <= 40:
    print("Adulto")
else:
    print("Veterano")