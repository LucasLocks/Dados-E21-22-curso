#ex036f.py

frase = str(input('Digite uma palavra ou frase: ')).strip().upper()

#transforma frase ou palavras em lista
palavras = frase.split()
#print(palavras)
#print(type(palavras))

#junta todas as palavras
caracteres = ''.join(palavras)
#print(caracteres)
#print(type(caracteres))

tamanho = (len(caracteres))
#print(tamanho)

#exemplo:
#Lucas
#01234

fraseinvertida = ''
for i in range((tamanho-1),-1,-1):
    #print(caracteres[i],end= '')
    fraseinvertida += caracteres[i]
    print(fraseinvertida,end='')

if fraseinvertida == caracteres:
    print('\nÉ um palíndromo !')
else:
    print('\nNão é palíndromo !')
#range(inicio, fim, passo)
#for i in range(0,10,1):
    #print(i)