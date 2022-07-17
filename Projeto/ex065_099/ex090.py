#ex090.py
""" Crie um programa que recebe do usuário uma sequencia de números aleatórios
separados por vírgula, armazene os números um a um, em formato de texto, como
elementos ordenados de uma lista. Mostre em tela a lista com seus respectivos
elementos após serem ordenados. """

"""
 qua = int(input("Quantos números você ira digitar: "))
lista = []
for x in range(0, qua):
    z = int(input("Digite o número: "))
    lista.append(z)

lista.sort()
print(f'Ordem crescente: {lista}') """

#v2:
numeros = []

num = input('Digite alguns números separados por vírgula: ').strip()
numeros = [int(val) for val in num.split(',')]

print(f'Aqui estão os números digitados sortidos: {(sorted(numeros))}')