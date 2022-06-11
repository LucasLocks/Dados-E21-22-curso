#dict.update.py

#dict.update = O método update() tanto pode criar, como atualizar dados:

dicio = {'nome': 'Erick'}

# Atualiza o elemento de chave 'nome'
dicio.update({'nome':'Matheus'})

# Cria os elementos de chave 'idade' e 'tamanho'
dicio.update({'idade':18})
dicio.update(tamanho=1.60)

print(dicio)

#resultado = {'nome': 'Matheus', 'idade': 18, 'tamanho': 1.60}