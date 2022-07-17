#ex096.py
"""Crie um programa que gera o valor de salário de funcionários considerando
apenas horas trabalhadas e horas extras, sendo o valor fixo de hora trabalhada
R$ 29,11 e do adicionas de hora extra R$ 5,00. Crie uma regra onde o
funcionário só tem direito a receber horas extras a partir de 40 horas
trabalhadas de forma convencional. """

horas_normais = int(input("Quantas horas normais trabalhadas: ")) * 29.11
extra= int(input("Quantas horas de horas extras: ")) * 5

pagamento = horas_normais + extra if (horas_normais >= 40) else horas_normais
print(f'Seu pagamento é de: {pagamento}')