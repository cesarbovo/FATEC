# Exercíco 10: Idade e sexo de alunos

total_homens = 0
total_mulheres = 0
soma_idade_homens = 0
soma_idade_mulheres = 0

for i in range(1, 11):  # 10 alunos
    print(f"\nAluno {i}:")
    
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    
    if sexo == 'M':
        total_homens += 1
        soma_idade_homens += idade
    elif sexo == 'F':
        total_mulheres += 1
        soma_idade_mulheres += idade
    else:
        print("Sexo inválido. Use apenas 'M' ou 'F'.")

# Cálculo das médias
media_idade_homens = soma_idade_homens / total_homens if total_homens > 0 else 0
media_idade_mulheres = soma_idade_mulheres / total_mulheres if total_mulheres > 0 else 0

# Resultados
print("\n--- Resultado ---")
print(f"Total de homens: {total_homens}")
print(f"Total de mulheres: {total_mulheres}")
print(f"Média da idade dos homens: {media_idade_homens:.2f}")
print(f"Média da idade das mulheres: {media_idade_mulheres:.2f}")
