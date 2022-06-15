#ex082.py

class Teste:
    var = 0
    def __init__(self):
        self.var = 1


print(Teste.var)
var = Teste()
print(var.var)