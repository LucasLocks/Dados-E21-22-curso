#ex045.py
#Crie um Dicionario de dados usando o construtor de dicionários do Python,
#alimente os valores do mesmo com os dados de duas listas Itens e Preços.

produtos = ['Pão','leite','café']
precos = ['9','5','18']

dc2 = dict(keys=produtos, values = precos)

print(dc2)
#{'keys': ['Pão', 'leite', 'café'], 'values': ['9', '5', '18']}