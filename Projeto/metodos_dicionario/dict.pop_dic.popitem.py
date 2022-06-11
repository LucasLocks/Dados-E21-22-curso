#dict.pop.py

"""dict.pop =  Excluindo e retornando o elemento excluído
O método pop() remove o item cujo a chave foi especificada: """

sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}

ovos = sacola.pop('ovos')

print(ovos)
print(sacola)

#resultado = {'maça': 2, 'farinha': 2}

"""dict.popitem =  diferente do método pop() que apenas retorna o valor daquele elemento,
popitem() retorna o elemento todo, contendo chave e valor.
Veja usando o mesmo exemplo do método pop(): """

sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}

farinha = sacola.popitem()

print(farinha)
print(sacola)

""" Veja que o retorno foi uma tupla e o último item foi removido:
('farinha', 2)
{'maça': 2, 'ovos': 6} """