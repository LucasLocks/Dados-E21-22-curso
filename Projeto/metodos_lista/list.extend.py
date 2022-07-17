#list.extend.py

""" list.extend = O extend()método adiciona todos os elementos de um iterável
(lista, tupla, string etc.) ao final da lista. """

numeros = [2, 3, 5]
num = [1, 4]

# Adiciona todos os elementos da lista numeros a lista num
num.extend(numeros)

print('Lista depois do extend():', num)

# Resultado: Lista depois do extend(): [1, 4, 2, 3, 5]