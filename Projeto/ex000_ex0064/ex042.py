#ex042.py
#Remova algum elemento da lista nomes.

from ex000 import nomes

nomes[1]='são'
nomes.insert(1,'e')
nomes.insert(2,'Java')
nomes.remove('uma')
print(nomes)