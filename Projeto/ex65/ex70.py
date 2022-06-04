""" Crie uma classe biblioteca que possui uma estrutura molde básica para
cadastro de um livro de acordo com seu titulo, porem que espera a inclusão de
um número não definido de títulos. Em seguida castre ao menos 5 livros nessa
biblioteca. (11) """

class Biblioteca():
    def __init__(self,livro1):
        self.livro1 = livro1

prateleira1 = Biblioteca('1450 = Bíblia de Gutenberg')
prateleira1.livro2 = '1984 = George'
prateleira1.livro3 = '19993 = azul'

print(prateleira1.livro1)
print(prateleira1.livro2)
print(prateleira1.livro3)



