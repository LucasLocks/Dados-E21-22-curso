#dict.items.py

""" dict.items = 'O items()método retorna um objeto de exibição que exibe uma lista
de pares de tuplas do dicionário (chave, valor).
""" 

marks = {'Physics':67, 'Maths':87}

print(marks.items())

# Resultado : dict_items([('Physics', 67), ('Maths', 87)])'

""" Percorrendo as chaves e valores de um Dicionário
Uma maneira de obter chaves e valores é utilizando o método dict.items(). """

frutas = {'pera': 10, 'uva': 2, 'maça': 55}

print(frutas.items())

""" A saída equivale a uma lista com elementos organizados em tuplas, sendo:
O primeiro elemento da tupla a chave do dicionário e
O segundo elemento, o valor presente naquela chave. """

#resultado: dict_items([('pera', 10), ('uva', 2), ('maça', 55)])