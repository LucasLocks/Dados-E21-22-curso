""" Crie uma classe biblioteca que possui uma estrutura molde básica para
cadastro de um livro de acordo com seu titulo, porem que espera a inclusão de
um número não definido de títulos. Em seguida castre ao menos 5 livros nessa
biblioteca. (11) """

class Biblioteca():
    def __init__(self,livro1,livro2,livro3,livro4,livro5):
        self.livro1 = livro1
        self.livro2 = livro2
        self.livro3 = livro3
        self.livro4 = livro4
        self.livro5 = livro5
        print(f'Livros Cadastrados : \n1 - {self.livro1}')
        print(f'2 - {self.livro2}')
        print(f'3 - {self.livro3}')
        print(f'4 - {self.livro4}')
        print(f'5 - {self.livro5}')

Biblioteca(
    livro1 = input('Digite o nome do 1° livro: '),
    livro2 = input('Digite o nome do 2° livro: '),
    livro3 = input('Digite o nome do 3° livro: '),
    livro4 = input('Digite o nome do 4° livro: '),
    livro5 = input('Digite o nome do 5° livro: ')
    )

