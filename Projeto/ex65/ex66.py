""" Crie uma classe Pessoa, instancie a mesma por meio de uma variável e crie
alguns atributos de classe dando características a essa pessoa. Por fim exiba
em tela alguma mensagem que incorpore os atributos de classe criados. """

class Pessoa:
    pass

pessoa1 = Pessoa()
pessoa1.nome = 'Lucas'
pessoa1.idade = 18
pessoa1.profissao = 'Professor'

print(f'{pessoa1.nome}, tem {pessoa1.idade} de idade , é um {pessoa1.profissao} ')
