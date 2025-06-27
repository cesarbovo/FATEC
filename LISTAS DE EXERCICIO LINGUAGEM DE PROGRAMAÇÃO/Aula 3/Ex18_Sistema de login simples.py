# Exercício 18: Sistema de login simples

usuario_correto = "admin"
senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido")
        break
    else:
        tentativas -= 1
        print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")
else:
    print("Acesso bloqueado")