# Exercício 9: Nota e média de cada aluno

for i in range(1, 7):  # 6 alunos
    print(f"\nAluno {i}:")
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / 2
    print(f"Média: {media:.2f}")
    
    if media <= 3.0:
        print("Condição: Reprovado")
    elif media <= 7.0:
        print("Condição: Exame")
    else:
        print("Condição: Aprovado")
