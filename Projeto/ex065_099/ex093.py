#ex093.py
""" Escreva uma função que recebe uma lista de elementos totalmente aleatórios
e os ordena de forma crescente de acordo com seu valor numérico: """

def ordena_lista(lista):
    for i in range(1,len(lista)):
        valor = lista[i]
        indice = i -1 
        while indice >= 0:            
            if valor < lista[indice]:
                lista[indice +1], lista[indice] = lista[indice], lista[indice +1]
                indice -=1
            else:
                break

    return lista

lista1 = ordena_lista([6,10,0,3,3,5,1,6,7,2,8,4])


print(lista1)