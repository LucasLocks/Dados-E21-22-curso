#dict.fromkeys.py

""" dict.fromkeys = O método cria um novo dicionário a partir da
sequência de elementos fornecida com um valor fornecido pelo usuário.

fromkeys()O método recebe dois parâmetros:
sequência - sequência de elementos que deve ser usado como chaves para o novo
dicionário
valor (opcional) - valor que é definido para cada elemento do dicionário

fromkeys()O método retorna um novo dicionário com a sequência de elementos
fornecida como as chaves do dicionário.
Se o argumento value for definido, cada elemento do dicionário recém-criado
será definido com o valor fornecido. 

Exemplo: Criar um dicionário a partir de uma sequência de chaves com valor
#teclas de vogais
"""
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vogal'

vowels = dict.fromkeys(keys, value)
print(vowels)

""" Resultado:
{'a': 'vogal', 'u': 'vogal', 'o': 'vogal', 'e': 'vogal', 'i': 'vogal'} """