#ex058.py
#Crie uma função que pode conter dois ou mais parâmetros, porem sem um numero
#definido declarado de parâmetros:

def msg(*args):
    print(f'Os parâmetros são: {args} ')

ex1 = msg('nome = Adriano','idade = 47','profissão = professor')