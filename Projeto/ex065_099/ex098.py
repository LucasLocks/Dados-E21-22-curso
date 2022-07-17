#ex098.py
""" Crie um programa que recebe uma nota entre 0 e 1.0, classificando de
acordo com a nota se o aluno fictício está aprovado ou em recuperação de acordo
com a sua nota. A média para aprovação deve ser 0.6 ou mais, e o programa deve
realizar as devidas validações para caso o usuário digite a nota
em um formato invalido. """

try:
    media =  float(input('Digite sua nota (0 a 1): '))     
    if (media >= 0.6 and media <= 1):
        aluno = "Aluno Aprovado"

    elif (media < 0.6 and media >= 0):
        aluno = "Aluno Reprovado"

    else:
        print('Valor invalido !' )

except:
    print('Digite apenas números !' )