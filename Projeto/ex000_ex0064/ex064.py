# ex064.py
numeros = (33,1987,2020)
dados = {'Nome':'Adriano','Profissão':'Professor'}

def id(*args,**kwargs):
    print(args)
    print(kwargs)
    print(kwargs['Nome'],' é ',kwargs['Profissão'])

id(*numeros,**dados)