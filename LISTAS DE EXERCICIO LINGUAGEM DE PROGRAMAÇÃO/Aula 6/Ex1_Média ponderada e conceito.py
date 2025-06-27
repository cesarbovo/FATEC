'''
Exercício 1
Pesos
Trabalho_lab = 2
Avaliacao_sem = 3
Exame_final = 5
'''
nota_Trabalho_lab = float(input(' Digite a nota do trabalho de laboratório do aluno entre 0 a 10: '))
nota_Avaliacao_sem = float(input(' Digite a nota da avaliação semestral do aluno entre 0 a 10: '))
nota_Exame_final = float(input(' Digite a nota do exame final do aluno entre 0 a 10: '))
media = ((nota_Trabalho_lab * 2) + (nota_Avaliacao_sem * 3) + (nota_Exame_final * 5))/10
media = round (media, 2)
if media >= 8 and media <= 10:
    print (f'A media do aluno é {media}, sendo o conceito A')
elif media >= 7:
    print (f'A media do aluno é {media}, sendo o conceito B')
elif media >= 6:
    print (f'A media do aluno é {media}, sendo o conceito C')
elif media >= 5:
    print (f'A media do aluno é {media}, sendo o conceito D')
else:
    print (f'A media do aluno é {media}, sendo o conceito E')