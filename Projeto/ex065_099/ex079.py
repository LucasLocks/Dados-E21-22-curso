#ex079.py
""" Escreva um programa que recebe do usuário um número de 0 a 100 e transcreve
o mesmo por extenso."""

from num2words import num2words

num = int(input('Digite um número: '))

if num <= 100 and num >= 0:
    num_extenso = num2words(num, lang='pt-br')
    print(f'Número digitado: {num_extenso}')
else:
    print('Número invalido !')