#ex088.py
""" Escreva uma função que recebe do usuário um número qualquer e retorna para
o mesmo tal numero elevado ao quadrado (simples ok!). Crie uma documentação
para esta função que possa ser acessada pelo usuário diretamente via IDE:
(dica docstring e PEP8) """

def ao_quadrado(num):
    '''esta funcao recebe como parâmetro um número retornando ao usuario o resultado do número elevado ao quadrado'''
    return num ** 2

print(ao_quadrado(10))
print(ao_quadrado.__doc__)