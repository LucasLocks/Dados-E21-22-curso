#ex091.py
""" Escreva um programa da forma mais reduzida possível, que recebe do usuario
uma série de nomes, separando os mesmos e os organizando em ordem alfabética.
Em Seguida exiba em tela os nomes já ordenados. """

nomes = [ x for x in input('digite os nomes separados por virgula: ').upper().split(',')]
nomes.sort()
print(','.join(nomes))