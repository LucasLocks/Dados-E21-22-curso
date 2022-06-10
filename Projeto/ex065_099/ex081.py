#ex081.py
""" Crie um programa que gera uma senha aleatória, com um tamanho definido pelo
usuário: """

from random import choice
import string

tamanho_da_senha = int(input("Quantos dígitos você quer na sua senha? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(tamanho_da_senha):
  senha += choice(caracteres)

print("A senha gerada é: ",senha)