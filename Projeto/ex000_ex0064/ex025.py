#ex025.py
#Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem
#dizendo se tal número é PAR ou se é Impar:

num = int(input('Digite um número: '))
if (num % 2) == 0:
    print(f'{num} é par')
else:
    print(f'{num} é impar')