#ex026.py
"""
Crie uma variável com valor inicial 0, enquanto o valor dessa variável for igual
ou menor que 10, exiba em tela o próprio valor da variável. A Cada execução a
mesma deve ter seu valor atualizado, incrementado em 1 unidade.
"""
from turtle import delay

var = 0

while var <= 10:
    print(var)
    var = var + 1

print('Fim') 