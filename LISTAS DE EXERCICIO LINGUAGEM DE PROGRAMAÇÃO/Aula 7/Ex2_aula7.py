joao = {"arroz", "feijão", "macarrão", "leite"}
maria = {"leite", "café", "açúcar", "arroz"}

# A operação de diferença de conjuntos (maria - joao) retorna os elementos que estão em 'maria' mas não em 'joao'.
produtos_exclusivos_maria = maria - joao

print(produtos_exclusivos_maria)