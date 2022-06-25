#ex097.py
""" Reescreva o código anterior adicionando um mecanismo simples de validação
que verifica se os dados inseridos pelo usuário são de tipos numéricos,caso não
sejam, encerrar o processo. """

try:
    horas_normais = int(input("Quantas horas normais trabalhadas: ")) * 29.11
    extra= int(input("Quantas horas de horas extras: ")) * 5
    pagamento = horas_normais + extra if (horas_normais >= 40) else horas_normais

except:
    print("Digite apenas números inteiros !")
    quit()


print(f'Seu pagamento é de: {pagamento}')