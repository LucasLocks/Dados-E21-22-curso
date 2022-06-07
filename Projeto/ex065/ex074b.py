class Calculadora:
    result = 0

    def __init__(self, op, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        _f = str(num1) + str(self.op) + str (num2)
        self.result = eval(_f)

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
op = input('Informe o operador: ')

resultado = Calculadora(op, num1, num2)
print(resultado.result)