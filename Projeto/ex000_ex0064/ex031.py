#ex031.py
"""
Crie um programa que realiza a Progressão Aritmética de 20 elementos, com
primeiro termo e razão definidos pelo usuário.  (Progressão aritmética - Uma
progressão aritmética é uma sequência numérica em que cada termo, a partir do
segundo, é igual à soma do termo anterior com uma constante r. O número r é
chamado de razão ou diferença comum da progressão aritmética.)
"""

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

pa = termo+ (20-1)* razao
for i in range(termo,pa + razao, razao):
    print(i)