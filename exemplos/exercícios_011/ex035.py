#ex035.py
#Crie um programa que pede ao usuário um número qualquer, em seguida retorno se este número é primo ou não, caso não, retorne também quantas vezes esse número é divisível.

numero = int(input('Digite um número:'))
divisoes = 0

for i in range(1,numero + 1):
    print(f'i = {i} mod: {numero%i}')
    if numero %i == 0:
        divisoes += 1
        print(f'i:{i}, numero: {numero%i}')

if divisoes == 2:
    print(f'{numero} é primo!!!!')
    print(f'{numero} é divisivel por um ou por {numero}')
else:
    print(f'{numero} NÃO é primo')
    print(f'{numero} é divisível {divisoes} vezes')