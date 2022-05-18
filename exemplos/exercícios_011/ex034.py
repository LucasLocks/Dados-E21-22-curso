#ex034.py
#Crie um programa que realiza a contagem de 1 a 100, usando apenas números impares ao final do processo exiba em tela quantos números impares foram encontrados nesse intervalo, assim como a soma dos mesmos:

contador = 0
soma = 0

for x in range(1, 101):
    if x % 2 != 0:
        soma += x
        contador += 1
print(f'Foram encontrados {contador} numeros impares')
print(f'A soma é de: {soma}')
