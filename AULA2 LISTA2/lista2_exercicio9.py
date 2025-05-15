'''
Exercício 9: Convertendo Celsius para Fahrenheit
Crie uma variável celsius e atribua um valor numérico a ela.
Converta esse valor para Fahrenheit usando a fórmula:
fahrenheit = (celsius * 9/5) + 32
Exiba o resultado formatado:
"A temperatura de [celsius]°C corresponde a [fahrenheit]°F."
'''

print(f' \n\nConvertendo Celsius para Fahrenheit \n')
celsius=float(input('Digite uma temperatura em graus Celsius (ºC): ').replace(',','.'))
fahrenheit=float(celsius*9/5)+32
print(f'\033[31mA temperatura de {round(celsius,1)}ºC corresponde a {round(fahrenheit,1)}ºF\033[0m\n')
# o comando \031[31m muda o trecho para vermelho. 0m volta a cor original
#\033[33m é amarelo e \033[34m é azul