#ex086.py
""" A partir de uma lista composta apenas de dados numéricos, gere outra lista
usando list comprehension usando como base a lista anterior, compondo a nova
com valores dos elementos originais elevados ao cubo:
(lista1 = [1,2,3,4,5,6] ; lista2 = [i** 3 for i in lista1]) """

list1 = [1,2,3,4,5,6]
list2 = [x **3 for x in list1]

print("Lista1:", list1)
print("Lista2:", list2)