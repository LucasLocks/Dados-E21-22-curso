# main.py
from pessoa import Pessoa

""" classe importada do arquivo Pessoa:
class Pessoa:
    def __init__(self, nome, idade, altura, cidade):
        self.nome = nome
        self.idade = idade 
        self.altura = altura
        self.cidade = cidade """

pessoa1 = Pessoa('Lucas', 19, 1.78, 'Lages')
pessoa2 = Pessoa('Carol', 25, 1.60, 'Criciúma')

print(f'Nome: {pessoa1.nome}\nCidade: {pessoa1.cidade}\nIdade: {pessoa1.idade}\nAltura:{pessoa1.altura}')
print(f'\nNome: {pessoa2.nome}\nCidade: {pessoa2.cidade}\nIdade: {pessoa2.idade}\nAltura:{pessoa2.altura}')
