#for_loops_c.py

alunos = {
    'Adriano':'reprovado',
    'Silvia':'aprovado',
    'Josimar':'aprovado'
}

for n,s in alunos.items():
    print(n,s)
    
    if s == 'aprovado':
        print("Parabéns: ", n)