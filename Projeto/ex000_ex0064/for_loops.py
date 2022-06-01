#for_loops.py

palavras = ['gato', 'cachorro', 'cobra']

for p in palavras:
    print(p,len(p))

tamanho_lista = len(palavras)
t1 = tamanho_lista

for x in range(0,t1,1):
    print(x,":", palavras[x])