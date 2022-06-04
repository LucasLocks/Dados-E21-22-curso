""" Escreva um programa, (calculadora simples), de 4 operações, onde o usuário
escolherá entre uma das 4 operações (+-*/). Lembrando que o usuário digitará
apenas dois valores, e escolhera uma operação de matemática do menu.(22) """

class Calculadora:

    result = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcula(self):
        print('1 - somar\n2 - Subtrair\n3 - Multiplicar\n4- Dividir')
        op = int(input('Digite o número da op desejada: '))
        if op == 1:
            self.result = self.num1 + self.num2

        if op == 2:
            self.result = self.num1 - self.num2
        
        if op == 3:
            self.result = self.num1 * self.num2

        if op == 4:
            self.result = self.num1 / self.num2

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))

resultado = Calculadora(num1, num2)
resultado.calcula()
print(resultado.result)