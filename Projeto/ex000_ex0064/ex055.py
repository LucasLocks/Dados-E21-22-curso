#ex055.py
""" Crie uma função com dois parâmetros relacionados ao nome e sobrenome de uma
pessoa. A função deve retornar uma mensagem de boas vindas e esses dados devem
ser digitados pelo usuário. O resultado deve vir todo em minusculas. """

def boas_vindas(nome,sobrenome):
    print(f'Seja bem vindo: {nome} {sobrenome}')

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

pessoa = boas_vindas(nome,sobrenome)