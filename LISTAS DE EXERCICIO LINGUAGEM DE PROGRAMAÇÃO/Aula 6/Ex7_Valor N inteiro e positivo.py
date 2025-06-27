# Exercício 7: Valor N inteiro e positivo

def calcular_fatorial(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    return fatorial

# Solicita a quantidade de números a serem lidos
N = int(input("Quantos números deseja digitar? "))

if N <= 0:
    print("Por favor, informe um número inteiro positivo.")
else:
    for i in range(N):
        valor = int(input(f"Digite o {i+1}º número inteiro positivo: "))
        
        if valor < 0:
            print("Número inválido! Apenas valores positivos são permitidos.")
        else:
            fatorial = calcular_fatorial(valor)
            print(f"{valor}! = {fatorial}")
