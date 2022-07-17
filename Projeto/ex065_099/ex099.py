#ex099
""" Crie uma estrutura molde (orientada a objetos) para cadastro de veículos
tendo como características que os descrevem sua marca, modelo, ano, cor e valor
Cadastre ao menos três veículos, revelando seu numero identificador de objeto
alocado em memória, assim como o retorno esperado pelo usuário quando o mesmo
consultar tal veículo. """

class Carro:
    def __init__(self, marca=None, modelo=None, ano=None, cor=None, valor=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor

    def desc(self):
        desc_carro = f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}\nPreço: {self.valor}\n'
        return desc_carro


carro1 = Carro('Audi', 'A3', 2006, 'Preto', 'R$ 19.900')
carro2 = Carro('VW', 'voyage', 1996, 'Azul', 'R$ 50.000')
carro3 = Carro('Ferrari', '812 GTS', 2021, 'Vermelho', 'R$ 3.710.172')

print(f'Carro 1:\n{carro1.desc()}')
print(f'Carro 2:\n{carro2.desc()}')
print(f'Carro 3:\n{carro3.desc()}')