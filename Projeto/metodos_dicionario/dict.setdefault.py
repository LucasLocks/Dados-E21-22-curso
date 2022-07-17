#dict.setdefault.py

"""dict.setdefault() = O método  retorna o valor da chave especificada, e, caso a
chave não exista, a cria com o valor especificado. """

dicio = {'coleta': 'scrappy', 'dados': 200}

set_dados = dicio.setdefault('dados')

print(set_dados)
print(dicio)

""" Como a chave dados existe, ela é retornada:
200
{'coleta': 'scrappy', 'dados': 200} """

#Agora vamos adicionar apenas a chave sem valor, e outro com chave e valor:

dicio = {'coleta': 'scrappy', 'dados': 200}

set_data = dicio.setdefault('data')
set_teste = dicio.setdefault('teste', 1)

print(set_data)
print(set_teste)
print(dicio)

""" A saída resulta em:
None
1
{'coleta': 'scrappy', 'dados': 200, 'data': None, 'teste': 1}

O set_data que teve apenas atribuída uma chave, teve seu valor criado como None
enquanto set_teste teve o valor adicionado. """