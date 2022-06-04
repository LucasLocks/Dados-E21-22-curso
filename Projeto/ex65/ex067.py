""" Crie uma classe que armazena algumas características de um carro, em
seguida crie dois carros distintos, de características diferentes, usando
da classe para a construção de seu objetos/variáveis. """

class Carro:
    ano = 1975
    cor = 'PretoBranco'
    modelo = 'hatch'
    opcionais = 'vidro+trava'

carro1 = Carro()

carro2 = Carro()
carro2.ano = 2000
carro2.cor = 'azul'

print(carro1.ano)
print(carro1.cor)
print(carro1.modelo)
print(carro1.opcionais)

print(carro2.ano)
print(carro2.cor)
print(carro2.modelo)
print(carro2.opcionais)


