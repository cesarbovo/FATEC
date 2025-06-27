# Exercício 8 - Validador de senha simples

senha = input("Digite uma senha: ")
tem_tamanho = len(senha) >= 8
tem_especial = any(c in "!@#$%&*" for c in senha)

if tem_tamanho and tem_especial:
    print("Senha aceita.")
else:
    if not tem_tamanho:
        print("A senha deve ter pelo menos 8 caracteres.")
    if not tem_especial:
        print("A senha deve conter pelo menos um caractere especial (!@#$%&*).")
