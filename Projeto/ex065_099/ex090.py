#ex090.py
""" Crie um programa que recebe do usuário uma sequencia de números aleatórios
separados por vírgula, armazene os números um a um, em formato de texto, como
elementos ordenados de uma lista. Mostre em tela a lista com seus respectivos
elementos após serem ordenados. """

numeros = str(input("Digite números separados por virgula: "))

lista = numeros.split(',')
lista.sort()

print(lista)