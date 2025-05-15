'''
Exercício 10: Criando uma mensagem personalizada
Peça ao usuário que digite um nome e um evento especial (por exemplo, "Festa de Aniversário"). Armazene essas informações e exiba a seguinte mensagem formatada:
"Olá, [nome]! Você está convidado(a) para a [evento]. Esperamos por você!"
'''
print('\n\n\033[34mCRIANDO UMA MENSAGEM PERSONALIZADA!\033[0m\n')
nome=input('Digite o nome do convidado: ')
evento=input('Digite o evento: ')
data=input('Digite a data no formato (dd/mes/aaaa): ')
hora=input('Digite o horário do evento (h:mm): ')
local=input('Digite o local: ')
print(f'\n\033[33mOlá, \033[31m{nome}! \033[33mVocê está convidado(a) para a minha festa de {evento}!\nA qual será realizada em {data}, às {hora}hs, no seguinte endereço: {local}\n Espero por você!!!\n\nBeijos, César.\033[0m\n\n ')
