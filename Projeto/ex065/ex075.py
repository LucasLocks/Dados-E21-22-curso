#ex075.py
""" Crie uma funcao que recebe um número e retorna o mesmo dividido em duas
metades, sendo cada metade um elemento de uma lista. Sendo que a divisão deve
retornar apenas elementos tipo int sem perder nenhum valor """

def divide(n):
    return [n//2,n-n//2]

n = int(input('num:'))
print(divide(n))