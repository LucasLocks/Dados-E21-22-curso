#ex059.py
#Crie uma função de numero de parâmeros indefinido, que realiza a soma dos
#números repassados como parâmero, independentemente da quantidade de números:

def soma(*args):
    num = 0
    for x in args:
        num += x
    print(f'O resultado da soma é {num}')

soma = soma(18,43,99,1,50)