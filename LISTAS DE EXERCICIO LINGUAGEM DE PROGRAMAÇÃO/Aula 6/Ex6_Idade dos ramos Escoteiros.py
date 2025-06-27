# Exercício 6: Idade dos ramos Escoteiros

idade = int(input("Digite a idade do escoteiro: "))

if idade < 6:
    print("Idade inválida! A idade mínima para ser escoteiro é 6 anos.")
elif 6 <= idade <= 10:
    print("Categoria: Lobinho")
elif 11 <= idade <= 14:
    print("Categoria: Escoteiro")
elif 15 <= idade <= 17:
    print("Categoria: Sênior")
elif 18 <= idade <= 21:
    print("Categoria: Pioneiro")
else:
    print("Categoria: Líder")
