#list.pop.py

""" list.pop = O pop()método remove o item no índice fornecido da lista e
retorna o item removido. """

numeros = [2, 3, 5, 7]
# remove the element at index 2
remove_elemento = numeros.pop(2)

print('Elemento removido:', remove_elemento)
print('Lista atualizada:', numeros)

"""Resultado:
Elemento removido: 5
Lista atualizada: [2, 3, 7] """