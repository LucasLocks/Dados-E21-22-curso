#dict.get.py

""" dict.get = 'O get()método retorna o valor da chave especificada se a chave
estiver no dicionário.
 """

#Exemplo
marks = {'Physics':67, 'Maths':87}

print(marks.get('Physics'))


# resultado: 67'

#Exemplo 2: Como get() funciona para dicionários?
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))

print('Age: ', person.get('age'))

# valor não é fornecido
print('Salary: ', person.get('salary'))


# valor  é fornecido
print('Salary: ', person.get('salary', 0.0))
""" Resultado:
Nome: Phill
Idade: 22
Salário: Nenhum
Salário: 0,0 
"""