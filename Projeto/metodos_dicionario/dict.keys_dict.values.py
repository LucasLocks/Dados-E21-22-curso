#dict.keys.py

""" dict.keys = 'Se você deseja obter todas as (chaves) de um dicionário,use o método
keys(), A saída é um objeto do tipo dict_keys que equivale a uma lista 
com todas as chaves: """

computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250bg'}

print(computador.keys())

""" Resultado
dict_keys(['CPU', 'RAM', 'SSD']) """

#dict.values = 'Para obter apenas os valores das chaves em seu dicionário:'

notas = {'Mat': 5, 'Por': 7, 'His': 8}

print(notas.values())

""" A saída será uma lista com os valores de cada chave:
dict_values([5, 7, 8]) """