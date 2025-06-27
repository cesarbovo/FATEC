'''
Faça um programa e mostre a data no formato por extenso
'''

dia = int(input ('Digite o dia desejado '))
mes = int(input ('Digite o mes desejado '))
ano = int(input ('Digite o ano desejado '))

if mes == 1:
    print(f'{dia} de janeiro de {ano}')
elif mes == 2:
    print (f'{dia} de fevereiro de {ano}')
elif mes == 3:
    print(f'{dia} de março de {ano}')
elif mes == 4:
    print(f'{dia} de abril de {ano}')
elif mes == 5:
    print(f'{dia} de maio de {ano}')
elif mes == 6:
    print(f'{dia} de junho de {ano}')
elif mes == 7:
    print (f'{dia} de julho de {ano}')
elif mes == 8:
    print(f'{dia} de agosto de {ano}')
elif mes == 9:
    print(f'{dia} de setembro de {ano}')
elif mes == 10:
    print(f'{dia} de outubro de {ano}')
elif mes == 11:
    print(f'{dia} de novembro de {ano}')
else:
    print(f'{dia} de dezembro de {ano}')
