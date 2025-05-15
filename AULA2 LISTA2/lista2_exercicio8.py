'''
Exercício 8: Calculando desconto
Crie uma variável preco_original e atribua um valor numérico a ela.
Crie outra variável chamada desconto (em porcentagem, por exemplo, 10 para 10%). Calcule o preço final após o desconto e exiba a seguinte mensagem:
"O produto que custava [preco_original] com desconto de [desconto]% agora custa [preco_final].
'''
preço_original=float(input('Digite o valor original do produto: R$ ').replace(',','.'))
while True:
       desconto=float(input('Digite o percentual de desconto: ').replace(',','.'))
       if 0<= desconto <=100:
              break
       else:
              print(' O desconto se limita a 100%. Por favor insira um valor válido!')
              
preço_final= (preço_original*(100-desconto)/100)
print(f' O produto que custava R${round(preço_original,2)} com desconto de {desconto}% agora custa R${round(preço_final,2)})')

