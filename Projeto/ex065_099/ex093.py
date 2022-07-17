#ex093.py
""" Escreva uma função que recebe uma lista de elementos totalmente aleatórios
e os ordena de forma crescente de acordo com seu valor numérico: """

lista = []
def ordena_lista():
    qua = int(input("Quantos números você ira digitar: "))
    for x in range(0, qua):
        z = int(input("Digite o número: "))
        lista.append(z)
        lista.sort()
        

ordena_lista()
print(lista)