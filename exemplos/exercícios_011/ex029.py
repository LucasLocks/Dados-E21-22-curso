#ex029.py
#Crie um programa que le um valor de inicio e um valor de fim, exibindo em tela
# a contagem dos números dentro desse intervalo.

#Valor informado será o 1° número a aparecer
inicio = int(input('Digite valor para início: '))

#Valor informado - 1, será o ultimo número a aparecer
fim = int(input('Digite valor para fim: '))

for i in range(inicio, fim, 1):
    print(i)