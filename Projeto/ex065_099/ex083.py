#ex083.py
""" Crie um programa que recebe o número digitado pelo usuário, convertendo o
mesmo para algarismo de número Romano, exibindo em tela esse dado já convertido
Utilizar Class. """

n1 = int(input('Digite um numero: '))

def conversor(n1):

    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0

    while n1 > 0:
        for x in range(n1 // numeros[i]):
            numeral += romanos[i]
            n1 -= numeros[i]

        i += 1

    return numeral

print(conversor(n1)) 