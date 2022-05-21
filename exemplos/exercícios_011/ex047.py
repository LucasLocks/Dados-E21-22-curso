#ex0147.py
#Crie um programa que recebe dados de um aluno como nome e suas notas em supostos 3 trimestres de 
#aula, retornando um novo dicionario como o nome do aluno e a média de suas notas

aluno = [{
    'Nome': 'Adriano', 
    'Notas': [4.7,37.9,79.2]    
    }]

print("Fase1:------------")
print(aluno)

def calcula_media(aluno):
    print("Fase2:------------")
    notas = []
    for media in aluno:
        print(f"Aluno --> {media['Nome']}")
        temp = round(sum(media['Notas'])/len(media['Notas']),2)
        print(f"Notas: {media['Notas']}")
    notas.append({'Nome':media['Nome'],'Media das notas': temp})
    print (notas)

media_estudante = calcula_media(aluno)
print("Fase3:------------")
print(aluno)
