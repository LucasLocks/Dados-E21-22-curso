#ex047e.py

def calcula_media(aluno):
    boletim = []
    for i in aluno:        
        mr = round(sum(i['Notas'])/len(i['Notas']), 1)
        boletim.append({'Nome': i['Nome'], 'Media das notas': mr})
        mr1 = round(sum(i['Notas1'])/len(i['Notas1']), 1)
        boletim.append({'Nome': i['Nome1'], 'Media das notas': mr1})
    return boletim
aluno = [{
    'Nome': 'Adriano',
    'Notas': [70.7, 80.9, 90.2],
    'Nome1': 'Lucas',
    'Notas1': [80.5, 99.9, 100.0]
}]
bl = (calcula_media(aluno))
print(bl)
