#ex053.py
""" Crie uma função que recebe um nome como parâmetro e exibe em tela uma mensagem
de boas vindas. O nome deve ser fornecido pelo usuário incorporado na mensagem
de boas vindas da função: """

def msg(nome):
    print(f'Seja bem vindo {nome}')

nome = input('Digite seu nome: ')
nome = msg(nome)