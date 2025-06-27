# Exercício 4: Caixa Eletrônico

valor = int(input("Digite o valor para saque: "))

notas = [100, 50, 20, 10, 5, 2, 1]

print("Notas necessárias:")
for nota in notas:
    quantidade = valor // nota
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R${nota}")
    valor %= nota
