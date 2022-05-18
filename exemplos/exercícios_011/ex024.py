#ex024.py
#Crie duas variaveis com dois valores numéricos inteiros digitados pelo usuário, caso o valor do primeiro número for maior que o do segundo, exiba em tela uma mensagem de acordo, caso contrario, exiba em tela uma mensagem dizendo que o primeiro valor digitado é menor que o segundo.

num1 = int(input('Digite A: '))
num2 = int(input('Digite B: '))

if num1 > num2:
    print('A é maior que B')
elif num2 > num1:
    print('B é maior que A')
else:
    print('A e B são iguais')