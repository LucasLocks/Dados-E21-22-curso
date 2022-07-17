#ex092.py
""" Escreva um simples programa que recebe do usuário um número qualquer,
retornando ao mesmo se este número é um numero perfeito. """

x = int(input("Digite um número: "))

def num_perfeito(x):
    soma = 0
    for i in range(1, x):
        if x % i == 0:
            soma += i
    return soma == x


msg = " É " if num_perfeito(x) else " NÃO É"

print(f'O número {x} {msg} perfeito')