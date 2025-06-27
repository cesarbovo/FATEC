# Exercício 12 - Alunos matriculados

curso_a = {("Ana", 101), ("Carlos", 102), ("João", 103)}
curso_b = {("João", 103), ("Marina", 104), ("Carlos", 102)}

exclusivos_a = curso_a - curso_b
exclusivos_b = curso_b - curso_a
comuns = curso_a & curso_b

print("Exclusivos do curso A:")
for nome, mat in exclusivos_a:
    print(f"{nome} ({mat})")

print("\nExclusivos do curso B:")
for nome, mat in exclusivos_b:
    print(f"{nome} ({mat})")

print("\nMatriculados nos dois cursos:")
for nome, mat in comuns:
    print(f"{nome} ({mat})")
