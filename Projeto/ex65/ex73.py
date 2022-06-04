""" Escreva um programa que encontre todos os números que são divisíveis por 7,
mas que não são múltiplos de 5, entre 200 e 2200 (ambos incluídos). Os números
obtidos devem ser impressos em sequencia, separados por virgula e em uma única
linha.(5) """

#V Lucas
x = 200
while x < 2201:
    x += 1
    if (x % 5 != 0) and (x % 7 == 0):
        print(x, end=" , ")


""" 
V Professor
lista[]

for i in range(200,2201):
    if (x % 5 != 0) and (x % 7 == 0):
        lista.append(str(i))
print(','.join(lista)) """

""" 
V Fernando
for i in range(200,2200): 
    if(i%7 == 0 and i%5 != 0): 
        print(i, end=',') """
    