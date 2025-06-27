# Exercício 13 - Média dos alunos

boletim = {
    "Ana": (8.0, 7.5),
    "Carlos": (5.0, 6.0),
    "Beatriz": (9.0, 8.5),
    "Daniel": (6.0, 6.5)
}

medias = {}
for nome, notas in boletim.items():
    media = sum(notas) / len(notas)
    medias[nome] = media

print("Médias dos alunos:")
for nome, media in sorted(medias.items()):
    print(f"{nome}: {media:.2f}")

print("\nAprovados:")
for nome in sorted([n for n, m in medias.items() if m >= 7.0]):
    print(nome)

print("\nReprovados:")
for nome in sorted([n for n, m in medias.items() if m < 7.0]):
    print(nome)
