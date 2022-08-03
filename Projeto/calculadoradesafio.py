exp = []
class Calculadora:
    result = 0

    def __init__(self, num1) -> None:
        self.num1 = num1
        self.result = eval(num1)


def calcula():
    num1 = str(input("Digite a expressão: "))
    calculadora1 = Calculadora(num1)
    exp.append(f'{calculadora1.num1} = {calculadora1.result}')
    resp = str(input("Quer continuar (S ou N): ")).upper()
    if resp == 'N':
        print(exp)
    if resp == 'S':
        calcula()

calcula()