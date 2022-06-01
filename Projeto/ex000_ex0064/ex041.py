#ex041.py
#Adicione um elemento na segunda posição da lista nomes.

from ex000 import nomes

nomes[1]= 'são'
nomes.insert(1, 'e')
nomes.insert(2, 'java')
print(nomes)