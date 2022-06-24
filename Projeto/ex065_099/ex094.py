#ex094.py
""" Crie uma estrutura toda orientada a objetos que recebe do usuário uma
string qualquer, retornando a mesma com todas as suas letras convertidas para
maiúsculas. Os métodos de classe para cada funcionalidade devem ser
independentes entre si, porem trabalhar no escopo geral da classe. Chame no
escopo global do programa cada um dos métodos. """

class Conversor():
    def __init__(self):
        self.s = input('Digite uma palavra/frase: ')

    def exibe_string(self):
        print(self.s.upper())


frase1 = Conversor()
frase1.exibe_string()