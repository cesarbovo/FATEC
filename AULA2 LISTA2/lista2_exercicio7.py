'''
Exercício 7: Criando um identificador de usuário
Peça ao usuário que digite seu primeiro nome e ano de nascimento.
Crie um identificador concatenando o nome com o ano e exiba o resultado.
Exemplo de entrada:
primeiro_nome = "Carlos" ano_nascimento = 1995
Saída esperada:
"Seu identificador de usuário é: Carlos1995"
'''
nome=input('Digite o seu primeiro nome: ')
nascimento=input('Digite o seu ano de nascimento: ')
print(f' O seu identificador de usuário é: {nome+nascimento}')
