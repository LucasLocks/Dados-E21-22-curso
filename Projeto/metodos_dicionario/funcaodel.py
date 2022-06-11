#funcaodel.py

""" Você pode excluir um elemento do dicionário com a keyword del do Python,
especificando sua chave: """

pessoa = {'nome': 'Matheus', 'idade': 18, 'tamanho': 1.60}

del pessoa['tamanho']

print(pessoa)
#Resultando = {'nome': 'Matheus', 'idade': 18}