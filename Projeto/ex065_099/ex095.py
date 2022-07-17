#ex095.py
""" Escreva de forma reduzida um programa que recebe do usuário um nome e duas
notas, salvando tais dados como um elemento de uma lista. Exiba em tela o
conteúdo desta lista. use: from operator import itemgetter """

from operator import itemgetter

aluno = []
x = str(input("Digite seu nome e suas 2 notas: "))
aluno = [x.split(',')]
print(sorted(aluno,key=itemgetter(0,1,2)))