'''
Exercício 5: Multiplicação de um número por uma string
Peça ao usuário que digite um número inteiro e armazene-o na variável numero.
Depois, peça que digite um caractere ou palavra curta e armazene-a na variável texto. Multiplique a string pelo número digitado e exiba o resultado:
Exemplo de entrada:
numero = 3 texto = "Python "
Saída esperada:
"Python Python Python "
'''
numero=int(input('Digite um numero inteiro: '))
texto=str(input('Digite um caracter ou uma palavra curta: '))
multiplicacao=numero*(texto+' ')
print(multiplicacao)