#dict.copy.py

""" 
dict.copy = 'Quando o copy()método é utilizado, é criado um novo dicionário que
é preenchido com uma cópia das referências do dicionário original.
"""

original = {1:'one', 2:'two'}
novo = original.copy()


print('Original: ', original)
print('Novo: ', novo)

""" 
Resultado:
Original: {1: 'um', 2: 'dois'}
Novo: {1: 'um', 2: 'dois'} 
"""