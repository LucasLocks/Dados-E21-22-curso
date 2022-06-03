""" Crie uma classe Inventario com os atributos de classe pré definidos item1 e
item2, a serem cadastrados manualmente pelo usuario, simulando um simples
carrinho de compras. (7) """

#V1

class Inventario:
    def __init__(self,item1,item2):
        self.item1 = item1
        self.item2 = item2
        print(f'Voce comprou {self.item1} e {self.item2}')

prod1 = Inventario(item1 = str(input('Qual o 1 item: ')),item2 = str(input('Qual o 2 item: ')))