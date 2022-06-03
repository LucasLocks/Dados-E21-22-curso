""" Mostre via terminal a string 'Bem vindo ao mundo da programação no entra21'
de trás pra frente utilizando indexação.(2) """

fraseinvertida = ''
frase = 'Bem vindo ao mundo da programação no entra21'
for i in range(len(frase)-1,-1,-1):
    fraseinvertida += frase[i]

print(fraseinvertida)