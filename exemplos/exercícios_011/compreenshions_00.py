# compreenshions_00.py

from numpy import append

# exemplo 1 
lista = list([1,3,6,9,10,12,13,15,2,4,5])
print(lista)
new_list = [x for x in lista if x > 5]
print(new_list)

#exemplo 2
lista = list([1,3,6,9,10,12,13,15,2,4,5])
print(lista)
new_list = []
for x in lista:
    if lista[x] > 5:
        new_list.append(x)
print(x)