# Exercício 20: Simulação de fila de atendimento

idade = int(input("Digite sua idade: "))
deficiente = input("É deficiente? (S/N): ").upper()
gestante = input("É gestante? (S/N): ").upper()

if deficiente == 'S' or idade >= 60:
    print("Prioridade máxima")
elif gestante == 'S':
    print("Prioridade média")
else:
    print("Atendimento normal")