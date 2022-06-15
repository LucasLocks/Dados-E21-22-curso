#ex082.py
""" Crie uma função que exibe em tela tanto o conteúdo de uma variável local
quando de uma variável global, sendo as variáveis de mesmo nome, porem uma não
substituindo a outra. (usar o comando: global <variável>)
v2 = Mesmo exercício fazendo com uma classe. """

var = False
def func():
    global var
    var = True
    return var

print(var)
print(func())
print(var)