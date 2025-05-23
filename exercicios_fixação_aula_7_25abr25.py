# -*- coding: utf-8 -*-
"""Exercicios fixação aula 7 25abr25.ipynb

'''
Exercício 1 – Itens em comum
Dado dois conjuntos representando os produtos comprados por duas pessoas no supermercado:
joao = {"arroz", "feijão", "macarrão", "leite"} maria = {"leite", "café", "açúcar", "arroz"}
'''
joao = {"arroz", "feijão", "macarrão", "leite"}
maria = {"leite", "café", "açúcar", "arroz"}
joao.intersection(maria)

'''
Exercício 2 – Itens exclusivos
Com os mesmos conjuntos:
joao = {"arroz", "feijão", "macarrão", "leite"} maria = {"leite", "café", "açúcar", "arroz"}
Quais produtos apenas Maria comprou, e João não comprou?
'''
joao = {"arroz", "feijão", "macarrão", "leite"}
maria = {"leite", "café", "açúcar", "arroz"}
maria.difference(joao)

'''
Exercício 3 – Lista sem repetição
Dada a seguinte lista de produtos (com duplicatas):
dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
Crie um conjunto a partir dessa lista para remover os itens repetidos e mostre os produtos únicos.
'''
dias = {"segunda", "terça", "quinta", "sexta", "sábado"}
dias1 = {"segunda", "terça", "quarta", "quinta", "sábado", "domingo"}
dias.union(dias1)

'''
Exercício 4 – Acesso por índice
Dada a tupla com os dias da semana:
dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
Imprima o primeiro, o terceiro e o último dia da semana.
'''
dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
print(dias[0], dias[2], dias[6])
print(dias [0])
print(dias[2])
print(dias[6])

'''
Exercício 5 – Desempacotamento de tupla
Dada a tupla:
produto = ("Arroz 5kg", 24.90)
Desempacote a tupla em duas variáveis chamadas nome e preco, e depois exiba uma mensagem formatada como:
O produto Arroz 5kg custa R$ 24.90.
'''
produto = ("Arroz 5kg", 24.90)
nome, preco = produto
print(f"O produto {nome} custa R$ {preco}.")

'''
Exercício 6 – Tupla de tuplas
Considere a seguinte tupla com informações de produtos:
carrinho = (     ("Arroz", 24.90),
    ("Feijão", 8.50),
    ("Leite", 4.80),
)
Percorra os itens do carrinho e exiba uma lista com os produtos e seus preços, um por linha, no formato:
Produto: Arroz | Preço: R$ 24.90
'''
carrinho = (("Arroz", 24.90), ("Feijão", 8.50), ("Leite", 4.80))
for produto in carrinho:
    print(f"Produto: {produto[0]} | Preço: R$ {produto[1]}")

'''
Exercício 7 – Acesso a valores
Dado o dicionário:
tabela = {     "Arroz": 24.90,
    "Feijão": 8.50,
    "Leite": 4.80,
    "Açúcar": 3.90
}
Pergunta:
Imprima o preço do "Leite" e do "Feijão".
'''
tabela = {"Arroz": 24.90, "Feijão": 8.50, "Leite": 4.80, "Açúcar": 3.90}
print(tabela["Leite"])
print(tabela["Feijão"])

'''
8 – Adição e atualização
Com o mesmo dicionário tabela, faça o seguinte:
Adicione um novo item: "Café" com valor 14.20. Atualize o preço do "Açúcar" para 4.10.
Imprima o dicionário atualizado.
'''

tabela = {"Arroz": 24.90, "Feijão": 8.50, "Leite": 4.80, "Açúcar": 3.90}
tabela["Café"] = 14.20
tabela["Açúcar"] = 4.10
print(tabela)

'''
Exercício 9 – Iteração sobre o dicionário
Use o dicionário:
compras = {
    "Sabonete": 2.50,
    "Shampoo": 15.00,
    "Condicionador": 16.50
}
Pergunta:
Percorra o dicionário e exiba cada item no formato:
Sabonete: R$ 2.50
'''
compras = {
    "Sabonete": 2.50,
    "Shampoo": 15.00,
    "Condicionador": 16.50
}
for item, preco in compras.items():
    print(f"{item}: R$ {preco}")

'''
Exercício 10 - Mini-Max Sum
Dados cinco inteiros positivos, encontre os valores mínimo e máximo que podem ser calculados somando exatamente quatro dos cinco inteiros. Em seguida, imprima os respectivos valores mínimo e máximo como uma única linha de dois inteiros longos separados por espaços.
Dado um lista de cinco inteiros positivos, encontre:
•	O menor valor possível da soma de quatro dos cinco inteiros.
•	O maior valor possível da soma de quatro dos cinco inteiros.
Depois, imprima os dois valores na mesma linha, separados por um espaço.
Entrada:
numeros = [1, 3, 5, 7, 9]
Saída:
16 24
Porque:
•	A menor soma possível (excluindo o maior número 9): 1 + 3 + 5 + 7 = 16
•	A maior soma possível (excluindo o menor número 1): 3 + 5 + 7 + 9 = 24
*Fonte: https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem? isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-monthpreparation-kit&playlist_slugs%5B%5D=three-month-week-one
'''
numeros = [1, 3, 5, 7, 9]
minimo = sum(numeros) - max(numeros)
maximo = sum(numeros) - min(numeros)
print(minimo, maximo)

'''
Exercício 11 - Top 3 Sum
Dada uma lista de números inteiros positivos, calcule:
A soma dos três maiores números da lista.
A soma dos três menores números da lista.
Imprima os dois valores na mesma linha, separados por espaço.
Entrada:
numeros = [10, 3, 5, 7, 2, 8, 12]
Saída:
10 32
'''
numeros = [10, 3, 5, 7, 2, 8, 12]
maiores = sorted(numeros)[-3:]
menores = sorted(numeros)[:3]
print(sum(maiores), sum(menores))

'''
Exercício 12 - "Alunos Matriculados"
Você recebeu duas listas com os alunos matriculados em dois cursos diferentes. Cada aluno é representado por uma tupla no formato:
(nome, matrícula)
Seu objetivo é:
Identificar os alunos que estão apenas no primeiro curso.
Identificar os alunos que estão apenas no segundo curso.
Identificar os alunos que estão matriculados nos dois cursos.
Entrada:
curso_a = {("Ana", 101), ("Carlos", 102), ("João", 103)} curso_b = {("João", 103), ("Marina", 104), ("Carlos", 102)}
Saída:
Exclusivos do curso A: Ana (101)
Exclusivos do curso B: Marina (104)
Matriculados nos dois cursos:
Carlos (102)
João (103)
'''
curso_a = {("Ana", 101), ("Carlos", 102), ("João", 103)}
curso_b = {("João", 103), ("Marina", 104), ("Carlos", 102)}
print("Exclusivos do curso A:")
for aluno in curso_a - curso_b:
    print(f"{aluno[0]} ({aluno[1]})")

print("\nExclusivos do curso B:")
for aluno in curso_b - curso_a:
    print(f"{aluno[0]} ({aluno[1]})")

print("\nMatriculados nos dois cursos:")
for aluno in curso_a & curso_b:
    print(f"{aluno[0]} ({aluno[1]})")

'''
Exercício 13 - "Alunos Matriculados"
Imprimir o nome de cada aluno e sua média.
Listar os alunos aprovados (média maior ou igual a 7.0). Listar os alunos reprovados (média menor que 7.0).
Mostre os nomes em ordem alfabética em cada categoria.
Entrada:
boletim = {
    "Ana": (8.0, 7.5),
    "Carlos": (5.0, 6.0),
    "Beatriz": (9.0, 8.5),
    "Daniel": (6.0, 6.5)
}
Saída:
Médias dos alunos:
Ana: 7.75
Beatriz: 8.75
Carlos: 5.50
Daniel: 6.25
Aprovados:
Ana Beatriz
Reprovados:
Carlos
Daniel
'''

boletim = {
    "Ana": (8.0, 7.5),
    "Carlos": (5.0, 6.0),
    "Beatriz": (9.0, 8.5),
    "Daniel": (6.0, 6.5)
}
print("Médias dos alunos:")
for aluno, notas in boletim.items():
    media = sum(notas) / len(notas)
    print(f"{aluno}: {media:.2f}")

print("\nAprovados:")
for aluno, notas in boletim.items():
    media = sum(notas) / len(notas)
    if media >= 7.0:
        print(aluno)

print("\nReprovados:")
for aluno, notas in boletim.items():
    media = sum(notas) / len(notas)
    if media < 7.0:
        print(aluno)

'''
Exercício 14 - "Número Inteiro para Romano"
Dado um número inteiro n no intervalo de 1 a 3999, converta esse número para sua representação
no sistema de números romanos.
Regras dos Números Romanos:
O sistema de números romanos usa as letras:
I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.
Para formar os números, usa-se a combinação de letras. O número é formado pela soma de valores
romanos. No entanto, quando um número menor vem antes de um número maior, ele é subtraído
(ex: IV = 4, IX = 9).
Objetivo:
Implemente uma função que receba um número inteiro n e retorne sua representação em números
romanos.
Exemplo de Entrada e Saída:
Entrada Saída
3 III
9 IX
58 LVIII
1994 MCMXCIV
2025 MMXXV
'''

def inteiro_para_romano(n: int) -> str:
    if n < 1 or n > 3999:
        raise ValueError("O número deve estar entre 1 e 3999.")

    pares = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    romano = ""
    for valor, simbolo in pares:
        while n >= valor:
            romano += simbolo
            n -= valor
    return romano

# Exemplo de uso
try:
    n = int(input("Digite um número inteiro (1-3999): "))
    print(inteiro_para_romano(n))
except ValueError as e:
    print(e)

->
