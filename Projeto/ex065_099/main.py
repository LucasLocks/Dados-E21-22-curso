# main.py
from pessoa import Pessoa

pessoa1 = Pessoa('Lucas', 19, 178, 'Lages')
pessoa2 = Pessoa('Carol', 25, 160, 'Criciúma')

print(f'Bem vindo Sr ,{pessoa1.nome}, parabéns pelos seus {pessoa1.idade} anos de vida')
print(f'Bem vindo Sra ,{pessoa2.nome}, parabéns pelos seus {pessoa2.idade} anos de vida')

""" 
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.altura)
print(pessoa1.cidade)

Exemplos anteriores ao video 7 
pessoa1 = Pessoa()
pessoa2 = Pessoa()

print('P1: ',pessoa1.nome)
print('P2: ',pessoa2.nome)

Pessoa.nome = 'Alex'

pessoa2.nome ='Adriano'

print('P1: ',pessoa1.nome)
print('P2: ',pessoa2.nome) """