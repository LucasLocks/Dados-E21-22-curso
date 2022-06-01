# ex060.py
#Crie uma função que recebe parâmetros tanto por justaposição (*args) quanto
#nomeados **(kwargs):

def id(*args,**kwargs):
    for n in args:
        nome = n
        print(f'{n}')
    
    for k,v in kwargs.items():
        idade = k
        sexo = v
        print(f'{idade},{sexo}')

        print(f'Nome:{nome},{idade},{sexo}')

id('Adriano', idade=47,sexo='M')
