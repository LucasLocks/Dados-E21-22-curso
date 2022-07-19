class Calculadora:
    result = 0

    def __init__(self, op, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        self.op = op
        _f = str(num1) + str(self.op) + str(num2)
        self.result = eval(_f)
        

num1 = str(input("Digite o numero: "))
op = input('Informe o operador: ').upper()
num2 = str(input("Digite o numero: "))
calculadora1 = Calculadora(op, num1, num2)
exp = (f'Resultados: {calculadora1.num1} {calculadora1.op} {calculadora1.num2} = {calculadora1.result}\n')

resp = str(input("Quer continuar (S ou N): "))
if resp == 'N':
    print(f'{num1} {op} {num2} = {calculadora1.result}')
if resp == 'S':
    chamaclasse