# ex047d.py

aluno = [{
    'Nome': 'Adriano', 
    'Notas': [70.7,80.9,90.2]    
    }]

for i in aluno:    
    print(f"Aluno {i['Nome']}")
    print(f"Notas {i['Notas']}")
    soma = sum(i['Notas'])
    print(f'Soma  {soma}')
    qtditens = len(i['Notas'])
    print(f'Itens  {qtditens}')
    media = soma/qtditens
    print(f'Media {media}')
    media_arredondada = round(media,1)
    print(f'Media arr {media_arredondada}')
    boletim = []
    boletim.append({'Nome':i['Nome'],'Media das notas': media_arredondada})
    print(boletim)