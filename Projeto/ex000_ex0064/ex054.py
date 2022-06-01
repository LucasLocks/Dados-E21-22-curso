#ex054.py
#Crie uma função que recebe um valor digitado pelo usuário e eleva esse valor
#ao quadrado.

def exp(num):
    return num **2

num = int(input('Digite um numero: '))
num = exp(num)

print(num)